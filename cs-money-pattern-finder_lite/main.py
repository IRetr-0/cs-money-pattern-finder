#remove useless imports l8r
import argparse
import os
import json
import requests
import shutil
import cv2
import numpy
import os
import sys
import pytesseract
from PIL import Image
from io import BytesIO

#These should not be global
global patterns_found
global found
global text_arr
patterns_found = []
found = []
text_arr = []

# defined command line options
# this also generates --help and error handling
CLI=argparse.ArgumentParser()

#skin ids - The search parameters for the skins; This should be a list of integers
CLI.add_argument(
  "--sids",  # name on the CLI - drop the `--` for positional/required parameters
  nargs="*",  # 0 or more values expected => creates a list
  type=int,
  default=[-1],  # default if nothing is provided
)

#pattern indexes - The search parameters for the patterns; This should be a list of integers
CLI.add_argument(
  "--pids",
  nargs="*",
  type=int,
  default=[-1],
)

#this is where the script will break if you're trying to run it, specially in linux
#btw if running in linux you'll need to invert a bunch of slashes on most if not all of the path strings
#This info should be in the readme, oh well.
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#This tries to download the image straight into a numpy array
#It doesn't use disk (that's good) but I got REALLY lazy with error handling so it sends a [0,1] array as errorcode????wtf
def load_image(url): 
	res = requests.get(url)
	try:
		img_arr = numpy.array(Image.open(BytesIO(res.content)))
	except OSError:
		x = numpy.arange(1)
		return x
	return img_arr

#gets the database from the provided URL. If they change it you should too
def getDatabase():
	#downloading the "nice, well organized and clean database"
	#btw my paths are weird, fix them
	path_to_database = os.path.dirname(os.path.abspath(__file__))+'\databases/load_bots_inventory.json'
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
		#sys.exit("Please use the included .bat file and enter the --sids param")
		return ids_list
	return ids_list

#Recieves a list of sids and downloads every image of every gun on the site.
def downloadImages(ids_list, patterns_searched):
	#junk lists cuz lazy
	ERROR = numpy.arange(1)
	url = []
	ids = []
	urllist = []
	
	path_to_database = os.path.dirname(os.path.abspath(__file__))+'\databases/load_bots_inventory.json'
	path_to_file = os.path.dirname(os.path.abspath(__file__))+'\images/'
	path_to_errimg = os.path.dirname(os.path.abspath(__file__))+'\databases/ERROR_CODE_0.jpg'
	
	with open(path_to_database,encoding="utf8") as f:
		#gets all the data from the json. This is super slow...
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
	#this is gonna get messy FAST
	#ok so this whole thing should be a function. Cuz this is where the program runs like everything
	for i in range (0,len(urllist)):#For every image it: downloads it, does some processing and extracts the text
		print("Getting text from image #",i)
		image_url = urllist[i]
		resp = load_image(image_url)
		if (resp.any() == ERROR):
			print("downloading of image #",i," failed - (0.0000000000 000)")
			resp = cv2.imread(path_to_errimg)
			proc_image = process_main(resp)
			read_main(patterns_searched, proc_image)
		else:
			proc_image = process_main(resp)
			read_main(patterns_searched, proc_image)
			
	del resp

#Downloads the most up-to-date database from csmoney as well as the images for analisis, who's ids are stored in ids_list that gets em' from the --sids param on the batch file
def images_main(list, list2):
	sids = setSearchParams(list)
	getDatabase()
	downloadImages(sids, list2)

#This processes the images in the most convoluted way I could think of. 
#It Resizes them to a set size since the site has like 5 different image standards
#Then it crops the images, some are crooked because there's guns that show 5 sticker slots and some that show only 4. This is because of CSmoney and I'm not fixing it
#Then it concatenates all images into a beeg long image. This was used with google drive + docs to OCR it. You can do that or just read it to sanity check the data you get 

def process_main(image):
	#Why have 4k images mixed with 2k and 1080ps at randon, why csmoney, why?
	resizedimg = cv2.resize(image,(1920,2620))
	crop_img = resizedimg[1305:1359, 530:971]#These coords are where the text we want is at
	return crop_img


#This big boy uses shitty image processing and tesseract ocr to extract text from all the images on the crop folder
#It spits out a 99% (more like 80%) accurate txt file with all the pattern ids of all the guns it analised (lol he said anal)
#BUT HOW DO I FIND THE GUN IN THE SITE? - Dum dum use the float value to filter the gun. 
#It's a long ass value so you'll find what you want in no time
#This info should be in the readme, oh well.
def read_main(patterns_searched, image):

	#shitty image processing. These all improve the accuracy of the OCR.
	image = cv2.resize(image, (0,0), fx=2, fy=2)#I downscale the images upthere only to scale them up again...
	thresh = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)[1]#idk
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
	close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
	result = cv2.GaussianBlur(close, (5,5), 0)#Makes things smooth
	
	text = pytesseract.image_to_string(result, config='--psm 11 -c tessedit_char_whitelist=.0123456789')#psm 11 or 10 works here
	#nooooooo don't do this =( shitty fix
	if text[1] != '.':#ok so if the text starts with the pattern value
		text_fix = text.split('\n')
		treated_text = text_fix[2] + '  ' + text_fix[0]#it needs to be swapped around

	else:#otherwise it's fine and I just need to remove the tons of \n that psm 11 ads	
		treated_text = text.replace('\n',' ')
	#isolates the pattern for each line.
	
	try:
		pattern = treated_text.split(' ')[2]
	#sometimes the OCR fails and pattern comes empty
	except IndexError:
		pattern = -1
	
	float = treated_text.split(' ')[0]#the float value is in the 0 and the pattern value is in the 2. 1 is just empty space
	text_arr.append(treated_text)
	#ok more "dumb solutions"
	#If the pattern the user searched for is present and it hasn't been already added, add it.
	if (int(pattern) in patterns_searched and int(pattern) not in patterns_found):
		patterns_found.append(pattern)
		found.append(float + '  ' + pattern)

#so when fixing the global stuff this will change.
#Right now it only prints the results at the end, but it should add them to the file everytime they get read
def writeResults():
	
	path_output = os.path.dirname(os.path.abspath(__file__))+'/output.txt'
	with open(path_output, "w") as txt_file:
			
			txt_file.write('Patterns found: ')
			for f in found:#just writes all the patterns the user searched for in neat text
				txt_file.write('[' + f + ']' + '  ')
			txt_file.write('\n\n')
			#Here it writes all the things that got found.
			#0.0000000000 000 means the image didn't download
			#and if the pattern is blank it probably means it's a 777 pattern or 77,
			#since the 7 in this font don't have a gap for each char, making them one HUGE char
			for line in text_arr:
				txt_file.write(line + '\n')

#it cobbles this mess togheter
def main():
	#loading parameters
	args = CLI.parse_args()
	print("Skin IDs to process: %r" % args.sids)
	print("Patterns you searched for: %r" % args.pids)
	images_main(args.sids,args.pids)#this calls all the other functions in it
	writeResults()
	
if __name__ == '__main__':
	main()
