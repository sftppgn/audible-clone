This program captures a screenshot and uses a computerized voice to read the text in the screenshot.  The program includes a loop to advance to the next page/slide/etc. by automatically clicking on a screen area that you define after it's finished reading the current location.  This can be used to play a kindle book like an audio book, text from pictures, presentations, slideshows, training, etc.  

The text contained in the image is extracted to a string "tesstr" prior to being voiced.  This step could be modified to save to file, check the text, etc.

**usage: python read.py**

You need to perform these steps, summarized here and explained in detail below.

#1 install tesseract 

#2 verify or change the tesseract path

#3 install other pip components

#4 adjust pixel locations

**#1 install tesseract**

Download and install tesseract from https://github.com/UB-Mannheim/tesseract/wiki.  You'll want to install it in C:\Program Files\Tesseract-OCR, or make note of where you install it due to the next requirement.

**#2 verify or change the tesseract path**

Line 20 contains the tesseract path.  You'll need to install tesseract to this location or change the line to match your tesseract location.

pytesseract.pytesseract.tesseract_cmd ="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

**#3 install other pip components**

pip install -r requirements.txt

where requirements.txt contains:

PyAutoGUI

numpy

pytesseract

opencv-python

Pillow

pyttsx3

**#4 adjust pixel locations**

Uncommenting lines 4 and 5 and running the program will activate a loop in the terminal that displays the mouse cursor location.  Use this to identify the pixel locations on your screen.

These are the pixel locations you'll need to change:

line 23:

change depending on your desired capture area, use the pyautogui commented out portion above to check xy coords - first set is top left, 2nd send is bottom right. (xtop, ytop, xbot, ybot)

    cap = ImageGrab.grab(bbox =(5, 110, 1335, 1032))
	
line 38:

this is the pixel location that you want to auto-click to advance the slide/page/etc. and start reading the next page.

pyautogui.click(x=1315, y=583)  

