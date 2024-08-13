#!/usr/bin/python3

### crypu.py ##
#
# RUN:	python3 crypu.py
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



def isBitString(a_string):
	is_only_bits = True
	for i in range(len(a_string)):
		if (a_string[i] != '0') and (a_string[i] != '1'):
			is_only_bits = False

	return is_only_bits





def main():
	# unpack args
	argc = len(sys.argv)

	if 1 < argc:

		if sys.argv[1] == "hash":
			path_in = ""
			data_in = ""
			key_in  = ""
			path_out = ""
			data_out = ""

			if 3 < argc:
				if argc == 4:
					# input data (text or bits) + key (text)
					raw_data = sys.argv[2]
					key_in   = sys.argv[3]

					if isBitString(raw_data):
						data_in = raw_data
						print("already bits")
					else:
						# convert to bit string
						print("needs converting")
				else:
					print("options not implemented yet...")
			
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


'''
teststr = "k!.7P2F-6Kj1,D2'2[{3YQ;9>R3'*!uP4qwgMK^w"
testkey = "password1"
bstr = stringToBinary(teststr)
bkey = stringToBinary(testkey)

hashed = xorHash(bstr, bkey)
saveHash("export.bin", hashed)
print("export.bin created.")

elif sys.argv[1] == "hash-from-file":
	testkey = "password"
	bkey = stringToBinary(testkey)
	hashedstr = loadHash("export.bin")
	print("export.bin loaded.")

	hashed = xorHash(hashedstr, bkey)
	teststr = binaryToString(hashed)
	print(teststr)
'''