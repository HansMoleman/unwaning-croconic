
### charencoding.py ##
#
# This module provides the ability to convert (encode/decode) character
# strings to bit strings, and bit strings to character strings.
#
# ---
#  R.C.H. (c) August 13, 2024
# ---
##



## binaryToString(str) : str
#
# Converts (decodes) a binary (bit) string to its corresponding
# character string, and returns the character string.
##
def binaryToString(binary_string):
	vstr = ""
	chunks = []

	curr_chunk = ""
	for i in range(len(binary_string)):
		curr_chunk += binary_string[i]

		if len(curr_chunk) == 32:
			chunks.append(curr_chunk)
			curr_chunk = ""

	for chunk in chunks:
		vchar = bytesToChar(chunk)
		vstr += vchar

	return vstr


## bytesToChar(str) : str
#
# Converts (decodes) a binary (bit) string to its corresponding
# character, then returns that character.
##
def bytesToChar(char_bytes):
	vascii = int(char_bytes, 2)
	return chr(vascii)


## charToBytes(chr) : str
#
# Converts (encodes) a character into its corresponding binary
# (bit) string, then returns the bit string.
##
def charToBytes(a_character):
	cbytes = ""
	vascii = ord(a_character)
	vbin   = bin(vascii)[2:]

	while((len(vbin) + len(cbytes)) < 32):
		cbytes += "0"
	cbytes += vbin

	return cbytes


## stringToBinary(str) : str
#
# Converts (encodes) a character string into its corresponding
# binary (bit) string, then returns that string.
##
def stringToBinary(a_string):
	bstr = ""

	for i in range(len(a_string)):
		cbytes = charToBytes(a_string[i])
		bstr += cbytes

	return bstr
