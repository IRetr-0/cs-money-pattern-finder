import pytesseract
import numpy as np
import cv2
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
DIR = 'D:/Downloads/xota/resize/crop'
n = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
text_arr = []
path = 'D:\\Downloads\\xota\\resize\\crop/'


for i in range (0, n):

	print("Reading image #",i)
	file = str(i) + 'imageC.jpg'
	image = cv2.imread(path+file,0)
	#processing
	thresh = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)[1]
	text = pytesseract.image_to_string(thresh, config='--psm 11 -c tessedit_char_whitelist=.0123456789')
	treated_text = text.replace('\n',' ')
	text_arr.append(treated_text)

	
with open("D:\\Downloads/output.txt", "w") as txt_file:
	for line in text_arr:
		txt_file.write(line+'\n')
