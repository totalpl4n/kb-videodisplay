@echo off
set /p filename=Enter your input video's name (including the file extension): 
set /p fps=Enter your desired output frame rate: 

echo.
echo Please ensure that the "frame" folder is completely clear before running the program, since it could cause problems later.
echo Please also ensure that ffmpeg has been installed. Learn how to install it in README.md.
echo.
pause


ffmpeg -i %filename% -vf "fps=%fps%,hue=s=0, scale=16:8" -start_number 0 .\frame\frame%%d.png