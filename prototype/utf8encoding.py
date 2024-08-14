
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
	vstring = ""
	characters = []

	sequence = ""
	i = 0
	while(i < len(binary_string)):
		if binary_string[i] == '0':
			# single byte
			for j in range(i, (i + 8)):
				sequence += binary_string[j]
			characters.append(sequence)

			sequence = ""
			i += 8

		elif binary_string[i] == '1':
			nbytes = 1

			j = 1
			while(binary_string[i + j] == '1'):
				nbytes += 1
				j += 1

			max_i = (nbytes * 8) + i
			for k in range(i, max_i):
				sequence += binary_string[k]
			characters.append(sequence)
			
			sequence = ""
			i += (nbytes * 8)

	# assemble characters to build string
	for char in characters:
		vstring += bytesToChar(char)

	return vstring


## bytesToChar(str) : str
#
# Converts (decodes) a binary (bit) string to its corresponding
# character, then returns that character.
##
def bytesToChar(char_bits):
	cbytes = bytes(char_bits, "UTF-8")
	vchar  = cbytes.decode()
	return vchar


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
