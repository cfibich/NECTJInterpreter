# Name:      nectjmain.py
# Author:    Chris Fibich
# Institute: University of Nebraska at Omaha
# Class:     CSCI 4220
# Date:      December 5, 2013
#
# Description: 
# An interpreter for the imperative language named
# NECTJ (Not Even Close To Java).

import sys
import nectjint
	
def main():

	# Handle command line arguments
	if len(sys.argv) == 1:
		nectjint.handle_error(nectjint.ERR_NOFILE, nectjint.USAGE_STR)
	elif len(sys.argv) > 2:
		nectjint.handle_error(nectjint.ERR_ARGS, nectjint.USAGE_STR)
	else:
		fileName = sys.argv[1]
		print fileName
		
		interpreter = nectjint.NECTJInterpreter(fileName)
		
		interpreter.RunInterpreter()

if __name__ == '__main__':
	main()
