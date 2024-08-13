
### hashing.py ##
#
# DPN:	None
#
# This module defines all logic related to hashing bit strings.
#
# ---
#  R.C.H. (c) August 12, 2024
# ---
##



##  xorHash(str, str) : str
#
# Carries out the process of XOR hashing the key string with
# the input string, where both strings are in binary form. The key
# wraps around any time the last character of it is used, and/so
# both input and key strings may be any length desired.
# Returns the hashed (bit) string produced.
##
def xorHash(input_bin, key_bin):
	str_hashed = ""

	i_key = 0
	for i in range(len(input_bin)):
		if input_bin[i] != key_bin[i_key]:
			str_hashed += '1'
		else:
			str_hashed += '0'

		if i_key == (len(key_bin) - 1):
			i_key = 0
		else:
			i_key += 1

	return str_hashed


## loadHash(str) : str
#
# Reads (binary) hashed data found within target file and
# returns it as a (bit) string.
##
def loadHash(filepath):
	bytes_in = None

	try:
		fobj = open(filepath, "rb")
		bytes_in = fobj.read()
		fobj.close()
	except:
		print("ERROR: could not open and/or read from target file; please check passed filepath and try again.")

	byte_str = ""
	if bytes_in:
		byte_str = bytes_in.decode()

	return byte_str


## saveHash(str, str) : None
#
# Writes (binary) hashed data from passed (bit) string to
# a binary file at passed file location.
##
def saveHash(filepath, bitstring):
	byte_str = bytes(bitstring, "UTF-8")

	try:
		fobj = open(filepath, "wb")
		bits = fobj.write(byte_str)
		fobj.close()
	except:
		print("ERROR: could not open and/or write to target file; please check passed filepath and try again.")
