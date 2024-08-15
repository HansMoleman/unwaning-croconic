
### utf8encoding.py ##
#
# This module provides the ability to convert (encode/decode) character
# strings to bit strings, and bit strings to character strings, following
# the UTF-8 encoding standard.
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
	nbytes = len(char_bits) / 8
	vchar = ''

	if nbytes <= 1:
		asc = int(char_bits, 2)
		vchar = chr(asc)
	
	else:
		chbits = ""

		if nbytes == 2:
			chbits += char_bits[3:8]
			chbits += char_bits[10:]
		elif nbytes == 3:
			chbits += char_bits[4:8]
			chbits += char_bits[10:16]
			chbits += char_bits[18:]
		else:
			chbits += char_bits[5:8]
			chbits += char_bits[10:16]
			chbits += char_bits[18:24]
			chbits += char_bits[26:]

		uni = int(chbits, 2)
		vchar = chr(uni)

	return vchar


## charToBytes(chr) : str
#
# Converts (encodes) a character into its corresponding binary
# (bit) string, then returns the bit string.
##
def charToBytes(a_character):
	cbytes = bytes(a_character, "UTF-8")
	bitstr = bin(int(cbytes.hex(), 16))[2:]

	'''
	if 8 < len(bitstr) and len(bitstr) < 16:
		padstr = "11"
		while((len(padstr) + len(bitstr)) < 16):
			padstr += '0'
		bitstr = padstr + bitstr
	'''

	return bitstr


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
