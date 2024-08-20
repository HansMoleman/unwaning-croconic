
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
##
def md5Hash(bitstr_in):
	block_size = 512
	lbits_size = 64

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

	# break message block down into 16 x 32-bit words
	pass


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
