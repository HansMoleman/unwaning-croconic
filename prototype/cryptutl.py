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
				fobj = open(hash_args["path_in"]["value"], 'r')
				txt_in = fobj.read()
				fobj.close()

				hash_args["data_in"]["value"] = txt_in
				hash_args["data_in"]["type"] = "txt"
				hash_args = stringToBinary(txt_in)

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
	if hash_args["path_ot"]["value"] != "":
		if hash_args["path_ot"]["type"] == "bin":
			saveHash(hash_args["path_ot"]["value"], hashed_bin)
		else:
			fobj = open(hash_args["path_ot"]["value"], 'w')
			fobj.write(binaryToString(hashed_bin))
			fobj.close()
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
			}
		}

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
			# file input option passed
			if sys.argv[2] == "-f":
				parse_dict["path_in"]["value"] = sys.argv[3]
				if sys.argv[3][-3:] == "bin":
					parse_dict["path_in"]["type"] = "bin"
				else:
					parse_dict["path_in"]["type"] = "txt"
				parse_dict["ukey_in"]["value"] = sys.argv[4]
				parse_dict["ukey_in"]["type"] = "txt"
			else:
				print("ERROR: weirdness...")

		elif argc == 6:
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
				print("ERROR: more weirdness")

		elif argc == 7:
			# file input and file output options passed
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
					print("ERROR: inner weirdness")
			else:
				print("ERROR: outer weirdness")

		return parse_dict

	else:
		if sys.argv[2] == "--help":
			print("help message for 'hash' command...")
			return None

		else:
			print(f"ERROR: command 'hash' expects a minimum of 2 arguments but {argc - 2} were given. Try argument '--help' with command for documentation.")
			return None



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


main()



# teststr = "k!$7P2F-6Kj1,D292[{3YQ;9>R32*!uP4qwgMK^w"
