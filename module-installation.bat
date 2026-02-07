@echo off
echo This program will install Pip, OpenCV, and NumPy.
pause

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
echo Please copy the path for pip before continuing.
pause

pip install opencv-python
pip install numpy