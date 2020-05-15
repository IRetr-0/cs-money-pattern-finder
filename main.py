import argparse
import getImages
import delImages
import processImages
import readImages

# defined command line options
# this also generates --help and error handling
CLI=argparse.ArgumentParser()
CLI.add_argument(
  "--sids",  # name on the CLI - drop the `--` for positional/required parameters
  nargs="*",  # 0 or more values expected => creates a list
  type=int,
  default=[-1],  # default if nothing is provided
)

def main():
	#delete old stuff
	delImages.del_main()
	
	#Download images
	args = CLI.parse_args()
	print("Skin IDs to process: %r" % args.sids)
	getImages.images_main(args.sids)
	
	#process the images
	processImages.process_main()

	#read the images
	readImages.read_main()
	
if __name__ == '__main__':
	main()