# cs-money-pattern-finder
It finds pattern indexes for weapons on the site csmoney

Run the "_run_pattern_finder.bat" file with the arg --sids with every unique skin id you want.
The included .bat file has the --sids arg set to every type of five-seven kami (stattraks and all floats)

Here's what all the files do - 

delImages - Deletes all the images from all the subfolders. Please run this BEFORE using the other files.

getImages - Downloads the database(json) that contains all items from the site and downloads the screenshots for all the unique weapons you want 

  oList = [1073306,171505] 
  #put in this list all the weapons you want, you can find the numbers for each gun in library-en-730.js
  #This is a list of two weapons - Stattrak AWP | WildFire (Factory New) - AWP | Neo-Noir (Factory New) -

processImages - Resizes, crops and concatenates all screenshots into one. You can find a "mega image" that you can use to sanity check the OCR text on the folder \images\resize\crop\megaimage - Otherwise I chose to read each image individually on the next file since it wielded better results

readImages - Analises each image and spits out text of what it thinks is on the image. I got this to a 'GOOD' degree of accuracy but it can still mess up, future updates MIGHT (lol no) fix this issue.

zoutput.txt is what it spits out.

This was made in python 3.7.#
You'll need some stuff to run it:

argparse
numpy
opencv
shutil
requests
json
pytesseract *

*With this last one needing to download an exe file also from: https://github.com/UB-Mannheim/tesseract/wiki
