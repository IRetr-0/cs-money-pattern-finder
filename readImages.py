#This big boy uses shitty image processing and tesseract ocr to extract text from all the images on the crop folder
#It spits out a 99% (more like 80%) accurate txt file with all the pattern ids of all the guns it analised (lol he said anal)
#BUT HOW DO I FIND THE GUN IN THE SITE? - Dum dum use the float value to filter the gun. 
#It's a long ass value so you'll find what you want in no time
#This info should be in the readme, oh well.

import pytesseract
import numpy as np
import cv2
import os
from PIL import Image

#this is where the script will break if you're trying to run it, specially in linux
#btw if running in linux you'll need to invert a bunch of slashes on most if not all of the path strings
#This info should be in the readme, oh well.
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#it does things
def read_main():	
	
	DIR = os.path.dirname(__file__)+'/images/resize/crop'
	path_output = os.path.dirname(__file__)+'/zoutput.txt'
	N = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
	text_arr = []

	for i in range (0, N):

		print("Reading image #",i)
		file = str(i) + 'imageC.jpg'
		image = cv2.imread(DIR+'/'+file,0)
		#shitty image processing. I need to add a blur here to improve accuracy
		thresh = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)[1]
		text = pytesseract.image_to_string(thresh, config='--psm 11 -c tessedit_char_whitelist=.0123456789')
		treated_text = text.replace('\n',' ')
		text_arr.append(treated_text)

	with open(path_output, "w") as txt_file:
		for line in text_arr:
			txt_file.write(line+'\n')
