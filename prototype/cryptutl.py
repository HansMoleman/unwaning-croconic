#!/usr/bin/python3

### cryptutl.py ##
#
# RUN:	python3 cryptutl.py
# DPN:	hashing.py, charencoding.py
#
# This is the main module for the 'unwaning-croconic' project prototype.
# The module is responsible for parsing user input and managing the rest of
# the system to accomplish the user's goal(s).
#
# ---
#  R.C.H. (c) August 13, 2024
# ---
##

import sys
from hashing import *
from charencoding import *



## isBitString(str) : bool
#
# Determines if given string is a bit string or not, and returns
# True if it is, False if it is not.
##
def isBitString(a_string):
	is_only_bits = True
	for i in range(len(a_string)):
		if (a_string[i] != '0') and (a_string[i] != '1'):
			is_only_bits = False

	return is_only_bits


##
#
#
##
def hashingOperation():
	pass





def main():
	# unpack args
	argc = len(sys.argv)

	if 1 < argc:
		if sys.argv[1] == "hash":
			path_in = ""
			data_in = ""
			type_in = ""
			key_in  = ""
			path_out = ""
			data_out = ""

			if 3 < argc and argc < 8:

				if argc == 4:
					# no options passed (input data + key only)
					raw_data = sys.argv[2]
					if isBitString(raw_data):
						data_in = raw_data
						type_in = "bin"
					else:
						data_in = stringToBinary(raw_data)
						type_in = "txt"
					key_in = stringToBinary(sys.argv[3])

				elif argc == 5:
					# file input option passed
					if sys.argv[2] == "-f":
						path_in = sys.argv[3]
						key_in = stringToBinary(sys.argv[4])
					else:
						print("ERROR: weirdness...")

				elif argc == 6:
					# file output option passed
					raw_data = sys.argv[2]
					if isBitString(raw_data):
						data_in = raw_data
						type_in = "bin"
					else:
						data_in = stringToBinary(raw_data)
						type_in = "txt"
					key_in = stringToBinary(sys.argv[3])

					if sys.argv[4] == "-f":
						path_out = sys.argv[5]
					else:
						print("ERROR: more weirdness")

				elif argc == 7:
					# file input and file output options passed
					if sys.argv[2] == "-f":
						path_in = sys.argv[3]
						key_in = stringToBinary(sys.argv[4])

						if sys.argv[5] == "-f":
							path_out = sys.argv[6]
						else:
							print("ERROR: inner weirdness")
					else:
						print("ERROR: outer weirdness")

				if data_in == "":
					if path_in[-3:] == "txt":
						fobj = open(path_in, 'r')
						txt_in = fobj.read()
						fobj.close()
						data_in = stringToBinary(txt_in)
						type_in = "txt"
					elif path_in[-3:] == "bin":
						data_in = loadHash(path_in)
						type_in = "bin"
					else:
						print("ERROR: incompatible file types detected...")

				data_out = xorHash(data_in, key_in)
				if path_out != "":
					if path_out[-3:] == "bin":
						saveHash(path_out, data_out)
					else:
						fobj = open(path_out, 'w')
						fobj.write(binaryToString(data_out))
						fobj.close()
					print(f"hash data saved to {path_out}.")
				else:
					if type_in == "bin":
						print(binaryToString(data_out))
					else:
						print(data_out)
					
			
			else:
				if sys.argv[2] == "--help":
					print("help message for 'hash' command...")
				else:
					print(f"ERROR: command 'hash' expects a minimum of 2 arguments but {argc - 2} were given. Try argument '--help' with command for documentation.")

			

		else:
			print("ERROR: unrecognized command; please try again with a valid command.")
	else:
		print("ERROR: no commands received; please try again with a recognized command (use command 'help' to see commands).")


main()



# teststr = "k!$7P2F-6Kj1,D292[{3YQ;9>R32*!uP4qwgMK^w"
