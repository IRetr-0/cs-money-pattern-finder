# cs-money-pattern-finder
It finds pattern indexes for weapons on the site csmoney


getimages.py = Image downloader for screenshots of every gun you want from the site.
In line 22: So the if ors here are all the items that you wanna fetch the URLs from, these are in the "o" of this weird json and can be found in a file named "library-en-730.js". Don't ask me how I know this.

makeMegaImage.py = crops, resises and combines all images onto one image, stacking them vertically. The cropped images are used in the next file -

ptAdventure.py = Is my adventure with a python lib called tesseract. This processes all images on the crop folder and extracts all text from them, compiling it all on the output.txt file

P.S

I didn't use root folders, for now atleast, so if using this alter the path of each file.
Sorry.
