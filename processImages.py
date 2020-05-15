import json
import requests
import cv2
import pytesseract
import numpy
import os

path_image = os.path.dirname(__file__)+'/images'
path_resize = os.path.dirname(__file__)+'/images/resize'
path_crop = os.path.dirname(__file__)+'/images/resize/crop'
path_megaimage = os.path.dirname(__file__)+'/images/resize/crop/megaimage'

#This uses the ammount of stuff in the dir, so make a image deleting script that runs before all this mess latter
n = len([name for name in os.listdir(path_image) if os.path.isfile(os.path.join(path_image, name))])

#resize
for i in range (0,n):
	print("resizing image #",i)
	downloadedimg = cv2.imread(path_image+'/'+str(i)+'image.jpg')
	rezisedimg = cv2.resize(downloadedimg,(1920,2620))
	cv2.imwrite(os.path.join(path_resize, str(i)+'imageR.jpg'), rezisedimg)
	cv2.waitKey(0)
print("Finished resizing 01")
#crop
for i in range (0,n):
	print("Cropping image #",i)
	rezisedimg = cv2.imread(path_resize+'/'+str(i)+'imageR.jpg')
	crop_img = rezisedimg[1305:1359, 530:971]
	cv2.imwrite(os.path.join(path_crop, str(i)+'imageC.jpg'), crop_img)
	cv2.waitKey(0)

print("Finished cropping")
	
#concat
img1 = cv2.imread(path_crop+'/'+str(0)+'imageC.jpg')
for i in range (0,n):
	print("Concatenating image #",i)
	img2 = cv2.imread(path_crop+'/'+str(i)+'imageC.jpg')
	img1 = cv2.vconcat([img1, img2])

print("Finished concatenating, you now have a MEGAIMAGE")
cv2.imwrite(os.path.join(path_megaimage, 'image.jpg'), img1)
cv2.waitKey(0)
