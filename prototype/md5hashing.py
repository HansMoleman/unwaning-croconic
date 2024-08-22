
### md5hashing.py
#
#
#
##

# test str: 'They are deterministic'
#      bit: '01010100011010000110010101111001001000000110000101110010011001010010000001100100011001010111010001100101011100100110110101101001011011100110100101110011011101000110100101100011'



## works
def getMessageLengthBits(msg_bitstr):
	nbits = len(msg_bitstr)
	nbits_bits = bin(nbits)[2:]

	output = ""
	while((len(output) + len(nbits_bits)) < 64):
		output += '0'
	output += nbits_bits

	return output


## WORKS
def modularAddition(x_bits, y_bits):
	# test_x:  '00000001001000110100010101100111'
	# test_y:  '11111110110111001011101010011000'
	x_int = int(x_bits, 2)
	y_int = int(y_bits, 2)
	z_int = (2**32)

	sumv = (x_int + y_int) % z_int
	sum_bits = bin(sumv)[2:]

	out_bits = ""
	while((len(sum_bits) + len(out_bits)) < 32):
		out_bits += '0'
	out_bits += sum_bits

	return out_bits


## WORKS
def bitAnd(x_bits, y_bits):
	# test_x:  '10001001101010111100110111101111'
	# test_y:  '11111110110111001011101010011000'
	andv = ""

	if len(x_bits) != len(y_bits):
		print("INTERNAL ERROR: bitAnd() requires the length of x_bits and the length of y_bits be equal.")
		exit(1)
	else:
		for i in range(len(x_bits)):
			if (x_bits[i] == '1') and (y_bits[i] == '1'):
				andv += '1'
			else:
				andv += '0'

	return andv


## WORKS
def bitOr(x_bits, y_bits):
	# test_x:  '10001000100010001000100010001000'
	# test_y:  '01110110010101000011001000010000'
	orv = ""

	if len(x_bits) == len(y_bits):
		for i in range(len(x_bits)):
			if (x_bits[i] == '0') and (y_bits[i] == '0'):
				orv += '0'
			else:
				orv += '1'

	else:
		print("INTERNAL ERROR: bitOr() requires x_bits and y_bits be of the same length.")
		exit(1)

	return orv


def bitNot(x_bits):
	pass


def bitXOR(x_bits, y_bits):
	pass