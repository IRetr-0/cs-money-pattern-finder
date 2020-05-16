import argparse
import getImages
import delImages
import processImages
import readImages

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

def main():
	#loading parameters
	args = CLI.parse_args()
	print("Skin IDs to process: %r" % args.sids)
	print("Patterns you searched for: %r" % args.pids)
	
	#delete old stuff
	delImages.del_main()
	
	#Download images
	getImages.images_main(args.sids)
	
	#process the images
	processImages.process_main()

	#read the images
	readImages.read_main(args.pids)
	
if __name__ == '__main__':
	main()