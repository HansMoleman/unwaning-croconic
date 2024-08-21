
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


## md5Hash(str) : str
#
# Computes the MD5 hash of the given input message (bitstring) and
# returns the corresponding 128-bit hash.
# Test Strings:
#	"This is a sample string for testing the MD5 hash method." (l=448)
#	"This is a sample string for testing MD5 hashing." (l=384)
##
def md5Hash(bitstr_in):
	block_size = 512
	lbits_size = 64
	init_a = "00000001001000110100010101100111"
	init_b = "10001001101010111100110111101111"
	init_c = "11111110110111001011101010011000"
	init_d = "01110110010101000011001000010000"
	k_const = [
		"11010111011010101010010001111000",
		"11101000110001111011011101010110",
		"00100100001000000111000011011011",
		"11000001101111011100111011101110",
		"00001111010101111100000011111010",
		"01000111100001111100011000101010",
		"10101000001100000100011000010011",
		"11111101010001101001010100000001",
		"01101001100000001001100011011000",
		"10001011010001001111011110101111",
		"11111111111111110101101110110001",
		"10001001010111001101011110111110",
		"01101011100100000001000100100010",
		"11111101100110000111000110010011",
		"10100110011110010100001110001110",
		"01001001101101000000100000100001",
		"11110110000111100010010101100010",
		"11000000010000001011001101000000",
		"00100110010111100101101001010001",
		"11101001101101101100011110101010",
		"11010110001011110001000001011101",
		"00000010010001000001010001010011",
		"11011000101000011110011010000001",
		"11100111110100111111101111001000",
		"00100001111000011100110111100110",
		"11000011001101110000011111010110",
		"11110100110101010000110110000111",
		"01000101010110100001010011101101",
		"10101001111000111110100100000101",
		"11111100111011111010001111111000",
		"01100111011011110000001011011001",
		"10001101001010100100110010001010",
		"11111111111110100011100101000010",
		"10000111011100011111011010000001",
		"01101001100111010110000100100010",
		"11111101111001010011100000001100",
		"10100100101111101110101001000100",
		"01001011110111101100111110101001",
		"11110110101110110100101101100000",
		"10111110101111111011110001110000",
		"00101000100110110111111011000110",
		"11101010101000010010011111111010",
		"11010100111011110011000010000101",
		"00000100100010000001110100000101",
		"11011001110101001101000000111001",
		"11100110110110111001100111100101",
		"00011111101000100111110011111000",
		"11000100101011000101011001100101",
		"11110100001010010010001001000100",
		"01000011001010101111111110010111",
		"10101011100101000010001110100111",
		"11111100100100111010000000111001",
		"01100101010110110101100111000011",
		"10001111000011001100110010010010",
		"11111111111011111111010001111101",
		"10000101100001000101110111010001",
		"01101111101010000111111001001111",
		"11111110001011001110011011100000",
		"10100011000000010100001100010100",
		"01001110000010000001000110100001",
		"11110111010100110111111010000010",
		"10111101001110101111001000110101",
		"00101010110101111101001010111011",
		"11101011100001101101001110010001"
	]

	# pad to 512-bits, or break down into chunks of 512-bits
	chunks = []
	if len(bitstr_in) < (512 - 64):
		# one chunk
		vchunk = ""
		for i in range(len(bitstr_in)):
			vchunk += bitstr_in[i]

		vchunk += '1'
		while(len(vchunk) < (512 - 64)):
			vchunk += '0'

		vchunk += messageLength(bitstr_in)

		if len(vchunk) == block_size:
			chunks.append(vchunk)
		else:
			print(f"INTERNAL ERROR: MD5 hashing requires a block size of 512 bits, but have {len(vchunk)} bits. Exiting...")
			exit(1)

	else:
		# multiple chunks
		offset = 0
		chunk = ""
		for i in range(len(bitstr_in)):
			if offset < (block_size - lbits_size):
				chunk += bitstr_in[i]
				offset += 1
			else:
				chunk_size = messageLength(chunk)
				chunk += '1'
				chunk += chunk_size
				if len(chunk) == block_size:
					chunks.append(chunk)
				else:
					print(f"INTERNAL ERROR: MD5 hashing requires a block size of 512 bits, but have {len(chunk)} bits. Exiting...")
					exit(1)

				offset = 0
				chunk = ""
				chunk += bitstr_in[i]
				offset += 1

		if 0 < offset:
			size_chunk = messageLength(chunk)
			chunk += '1'
			while(len(chunk) < (block_size - lbits_size)):
				chunk += '0'
			chunk += size_chunk
			chunks.append(chunk)

	print(chunks)
	message_chunk = chunks[0]	# only worry about single chunk case for now
	# bin of l=384 test string:
	# '010101000110100001101001011100110010000001101001011100110010000001100001001000000111001101100001011011010111000001101100011001010010000001110011011101000111001001101001011011100110011100100000011001100110111101110010001000000111010001100101011100110111010001101001011011100110011100100000010011010100010000110101001000000110100001100001011100110110100001101001011011100110011100101110'

	# break message block down into 16 x 32-bit words
	message_words = []
	word = ""
	counter = 0

	for i in range(len(message_chunk)):
		if counter == 32:
			message_words.append(word)
			word = ""
			counter = 0

		word += message_chunk[i]
		counter += 1
	message_words.append(word)
	
	print(f"num words:  {len(message_words)}")
	for mword in message_words:
		print(mword)


## messageLength(str) : str
#
# Measures the length of the passed message and converts the size from
# decimal to binary, and returns the binary string padded to 64 bits.
##
def messageLength(msg_bitstr):
	vsize = len(msg_bitstr)
	bsize = bin(vsize)[2:]

	size_bitstr = ""
	while((len(size_bitstr) + len(bsize)) < 64):
		size_bitstr += '0'
	size_bitstr += bsize

	return size_bitstr


def fFunction(bstr_b, bstr_c, bstr_d):
	# F(b, c, d) = (b & C) | ((!b) & d)
	b_and_c = ""
	not_b_and_d = ""
	b_and_c_or_not_b_and_d = ""


def gFunction(bstr_b, bstr_c, bstr_d):
	# G(b, c, d) = (b & d) | (c & (!d))
	pass


def hFunction(bstr_b, bstr_c, bstr_d):
	# H(b, c, d) = (b ^ c ^ d)
	pass

def iFunction(bstr_b, bstr_c, bstr_d):
	# I(b, c, d) = c ^ (b | (!d))
	pass


def modularAddition(bstr_x, bstr_y, bstr_z):
	int_x = int(bstr_x, 2)
	int_y = int(bstr_y, 2)
	int_z = int(bstr_z, 2)

	int_sum = (int_x + int_y) % int_z
	bin_sum = bin(int_sum)[2:]

	while(len(bin_sum) < 32):
		bin_sum = "0" + bin_sum

	return bin_sum


def bitshiftLeft(bit_string):
	pass


def hexToBinary(hex_string):
	bits = bin(int(hex_string, 16))[2:]

	while len(bits) < 32:
		bits = "0" + bits

	return bits


def binaryToHex(bit_string):
	hexv = hex(int(bit_string, 2))[2:]
	return hexv