import json
import requests
import shutil
import cv2
import pytesseract
import numpy
import os

#n = int(input("Ammount of images: "))

DIR = 'D:/Downloads/xota'

path_to_file = 'D:\\Downloads\\xota/'
path_to_file2 = 'D:\\Downloads\\xota\\resize/'
path_resize = 'D:/Downloads/xota/resize'
path_crop = 'D:/Downloads/xota/resize/crop'

path_to_file3 = 'D:\\Downloads\\xota\\resize\\crop/'
path_megaimage = 'D:/Downloads/xota/resize/crop/megaimage'

n = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

#resize
for i in range (0,n):
	print("resizing image #",i)
	downloadedimg = cv2.imread(path_to_file+str(i)+'image.jpg')
	rezisedimg = cv2.resize(downloadedimg,(1920,2620))
	cv2.imwrite(os.path.join(path_resize, str(i)+'imageR.jpg'), rezisedimg)
	cv2.waitKey(0)
print("Finished resizing 01")
#crop
for i in range (0,n):
	print("Cropping image #",i)
	rezisedimg = cv2.imread(path_to_file2+str(i)+'imageR.jpg')
	crop_img = rezisedimg[1305:1359, 530:971]
	cv2.imwrite(os.path.join(path_crop, str(i)+'imageC.jpg'), crop_img)
	cv2.waitKey(0)

print("Finished cropping")
	
#concat
img1 = cv2.imread(path_to_file3+str(0)+'imageC.jpg')
for i in range (0,n):
	print("Concatenating image #",i)
	img2 = cv2.imread(path_to_file3+str(i)+'imageC.jpg')
	img1 = cv2.vconcat([img1, img2])

print("Finished concatenating, you now have a MEGAIMAGE")
cv2.imwrite(os.path.join(path_megaimage, 'image.jpg'), img1)
cv2.waitKey(0)
