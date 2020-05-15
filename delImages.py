import os

path_image = os.path.dirname(__file__)+'/images'
path_resize = os.path.dirname(__file__)+'/images/resize'
path_crop = os.path.dirname(__file__)+'/images/resize/crop'
path_megaimage = os.path.dirname(__file__)+'/images/resize/crop/megaimage'

def del_main():
	print("Deleting older images...")
	for file in os.listdir(path_image): 
		if file.endswith('.jpg'):
			os.remove(path_image+'/'+file)
		
	for file in os.listdir(path_resize): 
		if file.endswith('.jpg'):
			os.remove(path_resize+'/'+file)
			
	for file in os.listdir(path_crop): 
		if file.endswith('.jpg'):
			os.remove(path_crop+'/'+file)
			
	for file in os.listdir(path_megaimage): 
		if file.endswith('.jpg'):
			os.remove(path_megaimage+'/'+file)