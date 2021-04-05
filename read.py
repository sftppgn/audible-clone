import pyautogui
import time

# while (True):
	# print (pyautogui.position())

import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab
import pyttsx3
engine = pyttsx3.init()

textarray=[]  
  
def imToString():
  
    # Path of tesseract executable
    #pytesseract.pytesseract.tesseract_cmd ="tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd ="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
   
    # change depending on your desired capture area, use the pyautogui commented out portion above to check xy coords - first set is top left, 2nd send is bottom right. (xtop, ytop, xbot, ybot)
    cap = ImageGrab.grab(bbox =(5, 110, 1335, 1032))
  
    # Converted the image to monochrome for it to be easily 
    # read by the OCR and obtained the output String.
    tesstr = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
            lang ='eng')
    return(tesstr)
  
while (True):
	textarray=imToString()
	
	engine.say(textarray)
	engine.runAndWait()
	time.sleep(1)
	pyautogui.click(x=1315, y=583)  
	time.sleep(1)