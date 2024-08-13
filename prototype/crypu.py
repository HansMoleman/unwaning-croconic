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



def main():
	# unpack args
	if 1 < len(sys.argv):

		if sys.argv[1] == "hash-to-file":
			teststr = "shdjgeproynapsdofnarkhn_3$5%&^2587%"
			testkey = "password"
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

		else:
			print("ERROR: unrecognized command; please try again with a valid command.")


main()