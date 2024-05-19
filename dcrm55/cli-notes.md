<!--
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop
$ cd dcrm55

saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ ls -la
total 5
drwxr-xr-x 1 saurav 197121  0 May 19 12:32 ./
drwxr-xr-x 1 saurav 197121  0 May 19 12:32 ../
drwxr-xr-x 1 saurav 197121  0 May 19 12:32 ./
drwxr-xr-x 1 saurav 197121  0 May 19 12:32 ../
drwxr-xr-x 1 saurav 197121  0 May 19 12:32 .git/
-rw-r--r-- 1 saurav 197121 40 May 19 12:33 README.md

saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ git push -u origin main
Enter passphrase for key '/c/Users/saurav/.ssh/id_rsa':
branch 'main' set up to track 'origin/main'.
Everything up-to-date

saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ git confid --global user.name "saurav"
git: 'confid' is not a git command. See 'git --help'.

The most similar command is
        config

saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ git config --global user.name "saurav"

saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ git config --global user.email "pankajbasnet2020@hotmail.com"

saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
error: remote origin already exists.

saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
error: remote origin already exists.

saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ git add .

saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ git commit -am "very important to add and commit before pushing"
[main 957a0e3] very important to add and commit before pushing
 1 file changed, 3 insertions(+)

saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ git push -u origin main
Enter passphrase for key '/c/Users/saurav/.ssh/id_rsa':
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Writing objects: 100% (3/3), 308 bytes | 308.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To github.com:pankaj-basnet/dcrm55.git
   e29fb40..957a0e3  main -> main
branch 'main' set up to track 'origin/main'.

saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$

saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ python -m venv venv

saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ source venv/Scripts/activate
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ pip install django
Collecting django
  Using cached Django-5.0.6-py3-none-any.whl.metadata (4.1 kB)
Collecting asgiref<4,>=3.7.0 (from django)
  Using cached asgiref-3.8.1-py3-none-any.whl.metadata (9.3 kB)
  Using cached sqlparse-0.5.0-py3-none-any.whl.metadata (3.9 kB)
Collecting tzdata (from django)
  Using cached tzdata-2024.1-py2.py3-none-any.whl.metadata (1.4 kB)
Using cached Django-5.0.6-py3-none-any.whl (8.2 MB)
Using cached asgiref-3.8.1-py3-none-any.whl (23 kB)
Using cached sqlparse-0.5.0-py3-none-any.whl (43 kB)
Using cached tzdata-2024.1-py2.py3-none-any.whl (345 kB)
Installing collected packages: tzdata, sqlparse, asgiref, django
Successfully installed asgiref-3.8.1 django-5.0.6 sqlparse-0.5.0 tzdata-2024.1
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ pip list
Package  Version
-------- -------
asgiref  3.8.1
Django   5.0.6
pip      24.0
sqlparse 0.5.0
tzdata   2024.1
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ python
Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import ys
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'ys'
>>> import sys
>>> print(sys.executable)
D:\src\PY\fcc-dcrm33--django\dcrm55-desktop\dcrm55\venv\Scripts\python.exe
>>> exit
Use exit() or Ctrl-Z plus Return to exit
>>> exit(
... )
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ python
Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> print(sys.executable)
D:\src\PY\fcc-dcrm33--django\dcrm55-desktop\dcrm55\venv\Scripts\python.exe
>>> pip list
  File "<stdin>", line 1
    pip list
        ^^^^
SyntaxError: invalid syntax
>>> exit()
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ pip install mysql
Collecting mysql
  Using cached mysql-0.0.3-py3-none-any.whl.metadata (746 bytes)
Collecting mysqlclient (from mysql)
  Using cached mysqlclient-2.2.4-cp312-cp312-win_amd64.whl.metadata (4.6 kB)
Using cached mysql-0.0.3-py3-none-any.whl (1.2 kB)
Using cached mysqlclient-2.2.4-cp312-cp312-win_amd64.whl (203 kB)
Installing collected packages: mysqlclient, mysql
Successfully installed mysql-0.0.3 mysqlclient-2.2.4
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ mysql-connector
bash: mysql-connector: command not found
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ pip install mysql-connector
Collecting mysql-connector
  Using cached mysql_connector-2.2.9-cp312-cp312-win_amd64.whl
Installing collected packages: mysql-connector
Successfully installed mysql-connector-2.2.9
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ pip install mysql-connector-python
Collecting mysql-connector-python
  Using cached mysql_connector_python-8.4.0-cp312-cp312-win_amd64.whl.metadata (2.0 kB)
Using cached mysql_connector_python-8.4.0-cp312-cp312-win_amd64.whl (14.5 MB)
Installing collected packages: mysql-connector-python
Successfully installed mysql-connector-python-8.4.0
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ django-admin startproject dcrm55
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55 (main)
$ cd dcrm55
(venv)
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55/dcrm55 (main)
$ python manage.py startapp website
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55/dcrm55 (main)
$ ls
dcrm55/  manage.py*  website/
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55/dcrm55 (main)
$ touch short-notes.md
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55/dcrm55 (main)
$ code short-notes.md
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55/dcrm55 (main)
$ touch cli-notes.md
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55/dcrm55 (main)
$ code short-notes.md
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55/dcrm55 (main)
$ code cli-notes.md
(venv)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src/PY/fcc-dcrm33--django/dcrm55-desktop/dcrm55/dcrm55 (main)
$
 -->
