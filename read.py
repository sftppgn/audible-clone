import pyautogui
import time

# while (True):
	# print (pyautogui.position())


# cv2.cvtColor takes a numpy ndarray as an argument
import numpy as nm

import pytesseract
  
# importing OpenCV
import cv2
  
from PIL import ImageGrab

import pyttsx3
engine = pyttsx3.init()
# engine.setProperty('voice', voices[1].id) 

textarray=[]  
  
def imToString():
  
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd ="tesseract.exe"
   
    # ImageGrab-To capture the screen image in a loop. 
    # Bbox used to capture a specific area.
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