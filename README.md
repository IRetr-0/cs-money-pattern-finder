# cs-money-pattern-finder

-OUTDATED-
-USELESS-
READ THIS FOR BASIC EXPLANATION OF WHY THIS SUX:
https://github.com/IRetr-0/cs-money-pattern-finder/issues/6






It finds pattern indexes for weapons on the site csmoney

For some reason the smart guys over a csmoney have the pattern index value listed in images for all skins, but not on the database as text??? This is a convoluted way of getting those values.

PLEASE use the 'lite' version of this included with the repo. This version stores a shit load of images and it's mainly use to debug the OCR. Once I'm done with this project (never) I'll delete this 'main' version

Run the "_run_pattern_finder.bat" file with the arg --sids with every unique skin id you want.
The included .bat file has the --sids arg set to every type of five-seven kami (stattraks and all floats)
new: --pids, put any patterns you want here and the program will add them to the top of the zoutput.txt file
the included .bat comes with it set to 909/662, the lewdest of patterns.

you can find skin ids on the included library-en-730.js file. You might (100% will have to) have to download this file since they'll update it with new skins all the time as they get released and added on their site

Here's what all the files do - 

delImages - Deletes all the images from all the subfolders.

getImages - Downloads the database(json) that contains all items from the site and downloads the screenshots for all the unique weapons you want 

processImages - Resizes, crops and concatenates all screenshots into one. You can find a "mega image" that you can use to sanity check the OCR text on the folder \images\resize\crop\megaimage . I chose to read each image individually on the next file since it got better results

readImages - Analises each image and spits out text of what it thinks is on the image. I got this to a 'GOOD' degree of accuracy but it can still mess up, future updates MIGHT (lol no) fix this issue. UPDATE, so I kinda did do a wee bit of image processing and I'm pretty sure is 100% accurate now. I got a friend (hostage) working on checking all the data to see if it's good;

zoutput.txt is the text that gets spat out.

This was made in python 3.7.#
You'll need some stuff to run it:

argparse; 
os; 
json; 
requests; 
shutil; 
cv2; 
numpy; 
os; 
sys; 
PIL - Image; 
io - BytesIO; 
pytesseract *; 

*With this last one needing to download an exe file also from: https://github.com/UB-Mannheim/tesseract/wiki
i might have forgotten to include all dependencies on this short list.
