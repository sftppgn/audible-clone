This program captures a screenshot and uses a computerized voice to read the text in the screenshot.  The program includes a loop to advance to the next screen, to read a kindle book like an audio book, similar to audible - but requiring the kindle cloud reader to be active on the screen.  It could also be used to read other written text, text from pictures, presentations, slideshows, training, etc.

You'll need to manually download and install tesseract.  Then you'll need to add the path to the program, or copy all of the files from the tesseract install location to the same base directory as the python program.

Download tesseract from here:  This is in addition to the pip install.
https://github.com/UB-Mannheim/tesseract/wiki

Line 20 is the line containing the path:
pytesseract.pytesseract.tesseract_cmd ="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

to install other requirements, run this:

python -r requirements.txt

where requirements.txt contains:
PyAutoGUI==0.9.50
numpy==1.20.2
pytesseract==0.3.7
opencv-python==4.5.1.48
Pillow==7.2.0
pyttsx3==2.90

You'll need to adjust the pixel locations. Uncommenting lines 4 and 5 will activate a loop in the terminal that displays the mouse cursor location.

These are the pixel locations:
line 23:
change depending on your desired capture area, use the pyautogui commented out portion above to check xy coords - first set is top left, 2nd send is bottom right. (xtop, ytop, xbot, ybot)
    cap = ImageGrab.grab(bbox =(5, 110, 1335, 1032))
	
line 38:
this is the pixel location that you want to auto-click to advance the slide/page/etc. and start reading the next page.
pyautogui.click(x=1315, y=583)  

