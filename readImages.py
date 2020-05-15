import pytesseract
import numpy as np
import cv2
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def read_main():	
	
	DIR = os.path.dirname(__file__)+'/images/resize/crop'
	path_output = os.path.dirname(__file__)+'/zoutput.txt'
	N = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
	text_arr = []

	for i in range (0, N):

		print("Reading image #",i)
		file = str(i) + 'imageC.jpg'
		image = cv2.imread(DIR+'/'+file,0)
		#processing
		thresh = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)[1]
		text = pytesseract.image_to_string(thresh, config='--psm 11 -c tessedit_char_whitelist=.0123456789')
		treated_text = text.replace('\n',' ')
		text_arr.append(treated_text)

	with open(path_output, "w") as txt_file:
		for line in text_arr:
			txt_file.write(line+'\n')
