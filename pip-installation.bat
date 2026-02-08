@echo off
echo This program will install Pip on your computer.
pause

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
echo Please copy the path for pip before ending this program.
pause
