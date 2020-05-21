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
def read_main(patterns_searched):	
	
	patterns_found = []
	found = []
	
	DIR = os.path.dirname(__file__)+'/images/resize/crop'
	path_output = os.path.dirname(__file__)+'/zoutput.txt'
	n = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
	text_arr = []

	for i in range (0, n):

		print("Reading image #",i)
		file = str(i) + 'imageC.jpg'
		image = cv2.imread(DIR+'/'+file,0)
		image = cv2.resize(image, (0,0), fx=2, fy=2)
		#shitty image processing. I need to add a blur here to improve accuracy
		thresh = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)[1]
		kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
		close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
		result = cv2.GaussianBlur(close, (5,5), 0)
		
		text = pytesseract.image_to_string(result, config='--psm 11 -c tessedit_char_whitelist=.0123456789')
		#nooooooo don't do this =( shitty fix
		if text[1] != '.':
			text_fix = text.split('\n')
			treated_text = text_fix[2] + '  ' + text_fix[0]
	
		else:	
			treated_text = text.replace('\n',' ')
		#isolates the pattern for each line.
		
		try:
			pattern = treated_text.split(' ')[2]
		#sometimes the OCR fails and pattern comes empty
		except IndexError:
			pattern = -1
		
		float = treated_text.split(' ')[0]
		text_arr.append(treated_text)
		if (int(pattern) in patterns_searched):
			patterns_found.append(pattern)
			found.append(float + '  ' + pattern)
		
	with open(path_output, "w") as txt_file:
		
		txt_file.write('Patterns found: ')
		for f in found:
			txt_file.write('[' + f + ']' + '  ')
		txt_file.write('\n\n')
		
		for line in text_arr:
			txt_file.write(line + '\n')
