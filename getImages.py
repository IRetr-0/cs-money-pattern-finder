#Downloads the most up-to-date database from csmoney as well as the images for analisis, who's ids are stored in ids_list that gets em' from the --sids param on the batch file

import json
import requests
import shutil
import cv2
import numpy
import os
import sys

#gets the database from the provided URL. If they change it you should too
def getDatabase():
	#downloading the nice, well organized and clean database
	
	path_to_database = os.path.dirname(__file__)+'\databases/load_bots_inventory.json'
	print("Downloading Database")
	url = "https://cs.money/730/load_bots_inventory"
	resp = requests.get(url, stream=True)
	file = ''
	local_file = open(path_to_database + file, 'wb')
	resp.raw.decode_content = True
	shutil.copyfileobj(resp.raw, local_file)
	print("complete")

#Sets the --sids from the batch. This is here just so the program doesn't run with no --sids input
def setSearchParams(ids_list):
	#list of 'o' to search
	#All the items that you wanna fetch the URLs from, these are in the "o" of this weird database and can be found in a file named "library-en-730.js" you can find it on their site.
	#Don't ask me how I know this.
	#dummy catcher
	if (-1 in ids_list):
		sys.exit("Please use the included .bat file and enter the --sids param")
	return ids_list

#Recieves a list of sids and downloads every image of every gun on the site.
def downloadImages(ids_list):
	#junk lists cuz lazy
	url = []
	ids = []
	urllist = []
	
	path_to_file = os.path.dirname(__file__)+'\images/'
	path_to_database = os.path.dirname(__file__)+'\databases/load_bots_inventory.json'
	path_to_errimg = os.path.dirname(__file__)+'\databases/ERROR_CODE_0.jpg'
	
	with open(path_to_database,encoding="utf8") as f:
		#gets all the data from the json. This is super slow
		data = json.load(f)

	N = len(data)

	#inefficiency at it's finest
	for i in range (0,N):
		try:
			if (data[i]['o'] in ids_list):
				#print(data[i]['id'], data[i]['o'], data[i]['d'])
				ids.append(data[i]['id'])#I never used this again, idk why it's still here.
				url.append(data[i]['d'])
		except KeyError:
			continue

	#my brain doesn't work so I SMASH
	flat_list = []#this was a matrix, guess what dum dum it's not one anymore it's a list get wreked newton
	for sublist in url:
		for item in sublist:
			flat_list.append(item)

	#https://s1.cs.money/HASHERE_image.jpg
	#20 why is this 20 here? oh I was gonna use slicing on the 20th char, lol, fuck that shit.
	for item in flat_list:
		item = "https://s1.cs.money/" + item + "_image.jpg"
		urllist.append(item)


	print("Ammount of images: ",len(urllist))
	#downloading the images, I think this is slow cuz of csmoney, but knowing my code...
	for i in range (0,len(urllist)):
		print("downloading image #",i)
		image_url = urllist[i]
		# Open the url image, set stream to True, this will return the stream content.
		resp = requests.get(image_url, stream=True)
		# Open a local file with wb ( write binary ) permission.
		file = str(i) + 'image.jpg'
		local_file = open(path_to_file+file, 'wb')
		# Set decode_content value to True, otherwise the downloaded image file's size will be zero.
		resp.raw.decode_content = True
		# Copy the response stream raw data to local image file.
		shutil.copyfileobj(resp.raw, local_file)
		# Remove the image url response object.
		size = os.path.getsize(path_to_file+file)
		#you can clearly tell these comments above are not written by me
		if (size == 0):
			print("downloading of image #",i," failed - (0.0000000000 000)")
			local_file = open(path_to_file+file, 'wb')
			error_file = open(path_to_errimg, 'rb')
			shutil.copyfileobj(error_file, local_file)
			
	del resp

#jank solution so the main file doesn't insta run when opened. Atleast it's not just a file with one func in it
def images_main(list):
	sids = setSearchParams(list)
	getDatabase()
	downloadImages(sids)