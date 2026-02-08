# kb-videodisplay
Play videos on a 16x8 matrix display. Optimized for the KidBright 32iA. This repository has been optimized for use on Windows only.


## Required Installations
### MicroBlock IDE 
Python IDE for programming the board.
<br>
Download: https://microblock.app/download

### Python
For converting the video's frames to bytes in order to play on the matrix display.
<br>
Download: https://www.python.org/downloads/

### FFmpeg
For converting the original video into a 16x8 frame sequence.
<br>
Download: https://ffmpeg.org/download.html
<br>
Tutorial: https://www.youtube.com/watch?v=JR36oH35Fgg

### Pip, OpenCV, NumPy
For installing the Python modules required to run the conversion script.
<br>
Installation can be done with the files provided.

<details>
 <summary>Tutorial</summary>
 
 1. Run *pip-installation.bat* and confirm by pressing any key.
 2. After it finishes running, copy the path specified near the end, and add it to the *Path* system variable.
 See how to do it [here.](https://www.youtube.com/watch?v=TqE4jBH4Me4&t=155s)
 3. Press any key to close the program, then run *module-installation.bat*. Make sure you've added the path to the system variable, then press any key to start installing the python modules.
</details>


## How to run the scripts
Once you've finished the installation, and you've downloaded the files provided, do as follows:

### 1. Paste your input video into this folder.
Once you have a video of your choice, preferably one that is 1-bit monochrome, paste it into the current folder containing these files.

### 2. Run *video-to-frames.bat*.
After pasting in the video file, run the script called *video-to-frames.bat* and input the name of the video from step 1, including its file extension. Then, input the final video's frame rate (without putting *fps*).  The frame count limit is 720. Here is a table for a video's **maximum** frame rate for its length.
| Video Length | Frame Rate |
| --- | ----------- |
| < 12 seconds | 60 fps |
| < 24 seconds | 30 fps |
| < 30 seconds | 24 fps |
| < 1 minute | 12 fps |
| < 2 minutes | 6 fps |
| < 3 minutes | 4 fps |
| < 4 minutes | 3 fps |
| < 6 minutes | 2 fps |
| < 12 minutes | 1 fps|

Formula for a video's **maximum** frame rate: <br>
```
720 / your video's length in seconds
```

### 3. Read the disclaimers displayed before continuing.
The program will display the disclaimers as follows:
```
Please ensure that the "frame" folder is completely clear before running the program, since it could cause problems later.
Please also ensure that ffmpeg has been installed. Learn how to install it in README.md.
```
Once you've ensured that both of these conditions have been met, press any key to start running the conversion program. This will convert your input video into 16x8 monochrome frames, ready to be processed by the next script.

**Reminder:** If this is your first time running the script, please delete the file titled *DELETEME* in the *frame* folder before pressing a key to continue.

### 4. Run *frame-to-text.py*.
Run the python script with the name *frame-to-text.py*. Once prompted, press enter to start the process. This will convert each frame of the video into bytes, which we will use in the main script that will be uploaded to the board. After the processing is done, copy everything between the two messages at the start and end. Once you've copied it, close the script.

**In case the script fails to run:** In the program's folder, type *cmd* into the directory at the top center. Then, type this command to run the script:
```
python frame-to-text.py
```

### 5. Open *run.mby* on MicroBlock IDE.
Open up MicroBlock IDE, click on *File* in the top left corner, then *Open*. Find run.mby in this folder, then open it. Paste in what you previoucly copied from step 4 into the variable *frames*. Then, put your frame rate from step 2 into the variable *framerate*.

### 6. Upload the code onto the board.
Once you've pasted in all of the variables, plug in your board with a USB cable, and click on the big upload button at the bottom center. 

After you've finished uploading, you can press *S1* on your board to play your video.


## Example Files
In the *examplefiles* folder, there are a few .mby files to test out different videos. To run them, follow steps *5* and *6*, without changing any variables.
