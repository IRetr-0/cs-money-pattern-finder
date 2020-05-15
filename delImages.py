#Deletes images in the folders specified on the __init__ section

import os

def del_main():
	
	#__init__
	path_image = os.path.dirname(__file__)+'/images'
	path_resize = os.path.dirname(__file__)+'/images/resize'
	path_crop = os.path.dirname(__file__)+'/images/resize/crop'
	path_megaimage = os.path.dirname(__file__)+'/images/resize/crop/megaimage'
	
	print("Deleting older images...")
	#image folder
	for file in os.listdir(path_image): 
		if file.endswith('.jpg'):
			os.remove(path_image+'/'+file)
		
	#resize folder
	for file in os.listdir(path_resize): 
		if file.endswith('.jpg'):
			os.remove(path_resize+'/'+file)
	#crop folder		
	for file in os.listdir(path_crop): 
		if file.endswith('.jpg'):
			os.remove(path_crop+'/'+file)
	#megaimage folder		
	for file in os.listdir(path_megaimage): 
		if file.endswith('.jpg'):
			os.remove(path_megaimage+'/'+file)