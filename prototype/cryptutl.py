#!/usr/bin/python3

### cryptutl.py ##
#
# RUN:	python3 cryptutl.py
# DPN:	hashing.py, utf8encoding.py
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
from utf8encoding import *



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


## doHashingOperation(dict) : None
#
# Uses the given argument dict to carry out a hashing operation as
# specified by the user.
##
def doHashingOperation(hash_args):
	source_bin = ""
	key_bin = ""
	hashed_bin = ""

	if hash_args["data_in"]["value"] == "":
			if hash_args["path_in"]["type"] == "txt":
				txt_in = loadTextString(hash_args["path_in"]["value"])

				hash_args["data_in"]["value"] = txt_in
				hash_args["data_in"]["type"] = "txt"
				source_bin = stringToBinary(txt_in)

			elif hash_args["path_in"]["type"] == "bin":
				hash_args["data_in"]["value"] = loadHash(hash_args["path_in"]["value"])
				hash_args["data_in"]["type"] = "bin"
				source_bin = hash_args["data_in"]["value"]

			else:
				print("ERROR: incompatible file types detected...")
	else:
		if hash_args["data_in"]["type"] == "txt":
			source_bin = stringToBinary(hash_args["data_in"]["value"])
		else:
			source_bin = hash_args["data_in"]["value"]

	key_bin = stringToBinary(hash_args["ukey_in"]["value"])

	hashed_bin = xorHash(source_bin, key_bin)
	if hash_args["data_ot"]["type"] != "":
		if hash_args["data_ot"]["type"] == "bin":
			print(hashed_bin)
		else:
			print(binaryToString(hashed_bin))

	elif hash_args["path_ot"]["value"] != "":
		if hash_args["path_ot"]["type"] == "bin":
			saveHash(hash_args["path_ot"]["value"], hashed_bin)
		else:
			saveTextString(hash_args["path_ot"]["value"], binaryToString(hashed_bin))

		otpath = hash_args["path_ot"]["value"]
		print(f"hash data saved to {otpath}.")
	
	else:
		if hash_args["data_in"]["type"] == "bin":
			print(binaryToString(hashed_bin))
		else:
			print(hashed_bin)


## parseHashCommand(int) : dict
#
# Determines what combination of arguments has been passed and then
# stores the argument values, along with their associated types,
# for the 'hash' command. Returns a dict containing the arg names as keys
# to their own dicts holding the value and type; only args present will be
# set and the others left blank.
##
def parseHashCommand(argc):

	if 3 < argc and argc < 8:
		parse_dict = {
			"data_in": {
				"value": "",
				"type": ""
			},
			"ukey_in": {
				"value": "",
				"type": ""
			},
			"path_in": {
				"value": "",
				"type": ""
			},
			"path_ot": {
				"value": "",
				"type": ""
			},
			"data_ot": {
				"value": "",
				"type": ""
			}
		}
		errors = 0

		if argc == 4:
			# no options passed (input data + key only)
			raw_data = sys.argv[2]
			if isBitString(raw_data):
				parse_dict["data_in"]["value"] = raw_data
				parse_dict["data_in"]["type"] = "bin"
			else:
				parse_dict["data_in"]["value"] = raw_data
				parse_dict["data_in"]["type"] = "txt"
			parse_dict["ukey_in"]["value"] = sys.argv[3]
			parse_dict["ukey_in"]["type"] = "txt"

		elif argc == 5:
			# either file input or format output passed
			if sys.argv[2] == "-f":
				# file input option passed
				parse_dict["path_in"]["value"] = sys.argv[3]
				if sys.argv[3][-3:] == "bin":
					parse_dict["path_in"]["type"] = "bin"
				else:
					parse_dict["path_in"]["type"] = "txt"
				parse_dict["ukey_in"]["value"] = sys.argv[4]
				parse_dict["ukey_in"]["type"] = "txt"

			elif (sys.argv[4] == '-b') or (sys.argv[4] == '-t'):
				# format for output as string specified
				raw_data = sys.argv[2]
				if isBitString(raw_data):
					parse_dict["data_in"]["value"] = raw_data
					parse_dict["data_in"]["type"] = "bin"
				else:
					parse_dict["data_in"]["value"] = raw_data
					parse_dict["data_in"]["type"] = "txt"
				parse_dict["ukey_in"]["value"] = sys.argv[3]
				parse_dict["ukey_in"]["type"] = "txt"

				if sys.argv[4] == '-b':
					parse_dict["data_ot"]["type"] = "bin"
				else:
					parse_dict["data_ot"]["type"] = "txt"

			else:
				print("ERROR: weirdness...")
				errors += 1

		elif argc == 6:
			# file output or file input + output format option passed
			if sys.argv[2] == "-f":
				# file input + output format options passed
				parse_dict["path_in"]["value"] = sys.argv[3]
				if sys.argv[3][-3:] == "bin":
					parse_dict["path_in"]["type"] = "bin"
				elif sys.argv[3][-3:] == "txt":
					parse_dict["path_in"]["type"] = "txt"
				else:
					print(f"ERROR: incompatible file type ({(sys.argv[3][-3:])}) for file input!")
					errors += 1

				parse_dict["ukey_in"]["value"] = sys.argv[4]
				parse_dict["ukey_in"]["type"] = "txt"

				if sys.argv[5] == "-b":
					parse_dict["data_ot"]["type"] = "bin"
				elif sys.argv[5] == "-t":
					parse_dict["data_ot"]["type"] = "txt"
				else:
					print(f"ERROR: expected arg \'-b\' or \'-t\' but received \'{sys.argv[5]}\'.")
					errors += 1

			else:
				# file output option passed
				raw_data = sys.argv[2]
				if isBitString(raw_data):
					parse_dict["data_in"]["value"] = raw_data
					parse_dict["data_in"]["type"] = "bin"
				else:
					parse_dict["data_in"]["value"] = raw_data
					parse_dict["data_in"]["type"] = "txt"
				parse_dict["ukey_in"]["value"] = sys.argv[3]
				parse_dict["ukey_in"]["type"] = "txt"

				if sys.argv[4] == "-f":
					parse_dict["path_ot"]["value"] = sys.argv[5]
					if sys.argv[5][-3:] == "bin":
						parse_dict["path_ot"]["type"] = "bin"
					else:
						parse_dict["path_ot"]["type"] = "txt"
				else:
					print(f"ERROR: expected arg \'-f\' but received \'{sys.argv[4]}\'; please try again.")
					errors += 1


		elif argc == 7:
			# file input and file output or file input and output format options passed
			if sys.argv[2] == "-f":
				parse_dict["path_in"]["value"] = sys.argv[3]
				if sys.argv[3][-3:] == "bin":
					parse_dict["path_in"]["type"] = "bin"
				else:
					parse_dict["path_in"]["type"] = "txt"
				parse_dict["ukey_in"]["value"] = sys.argv[4]
				parse_dict["ukey_in"]["type"] = "txt"

				if sys.argv[5] == "-f":
					parse_dict["path_ot"]["value"] = sys.argv[6]
					if sys.argv[6][-3:] == "bin":
						parse_dict["path_ot"]["type"] = "bin"
					else:
						parse_dict["path_ot"]["type"] = "txt"
				else:
					print(f"ERROR: expected arg \'-f\' but received \'{sys.argv[5]}\'.")
					errors += 1
			else:
				print(f"ERROR: expected arg \'-f\' but received \'{sys.argv[2]}\'.")
				errors += 1

	else:
		if sys.argv[2] == "--help":
			print("help message for 'hash' command...")
			errors += 1

		else:
			print(f"ERROR: command 'hash' expects a minimum of 2 arguments but {argc - 2} were given. Try argument '--help' with command for documentation.")
			errors += 1

	if 0 < errors:
		print("exiting!")
		exit(0)
	else:
		return parse_dict


## loadTextString(str) : str
#
# Loads a plain-text string from target text file and returns it. If the
# target file cannot be accessed, method signals system to exit.
##
def loadTextString(filepath):
	
	try:
		fobj = open(filepath, 'r')
		tstr = fobj.read()
		fobj.close()
		return tstr

	except:
		print("ERROR: could not access/read from target file!")
		exit(0)


## saveTextString(str, str) : None
#
# Saves a plain-text string to target text file. If the target file
# cannot be accessed, method signals system to exit.
##
def saveTextString(filepath, text_string):
	try:
		fobj = open(filepath, 'w')
		fobj.write(text_string)
		fobj.close()

	except:
		print("ERROR: could not access/write to target file!")
		exit(0)



def main():
	# unpack args
	argc = len(sys.argv)

	if 1 < argc:
		if sys.argv[1] == "hash":
			# parse hash command and execute
			hash_args = parseHashCommand(argc)
			doHashingOperation(hash_args)
		else:
			print("ERROR: unrecognized command; please try again with a valid command.")
	else:
		print("ERROR: no commands received; please try again with a recognized command (use command 'help' to see commands).")


if __name__ == "__main__":
	main()
else:
	print("cryptutl v2024.08.15 (prototype) module loaded.")



# teststr = "k!$7P2F-6Kj1,D292[{3YQ;9>R32*!uP4qwgMK^w"
