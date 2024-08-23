
### md5hashing.py
#
#
# August 22, 2024
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


## WORKS
def bitNot(x_bits):
	# test_x:  '10001001101010111100110111101111'
	# result:  '76543210'
	notv = ""

	for i in range(len(x_bits)):
		if x_bits[i] == '0':
			notv += '1'
		else:
			notv += '0'

	return notv


## WORKS
def bitXOR(x_bits, y_bits):
	# test_x:  '11010101000001110001001101100111'
	# test_y:  '11000000010110001010110111100010'
	# result:  '155fbe85'
	xorv = ""

	if len(x_bits) == len(y_bits):
		for i in range(len(x_bits)):
			if x_bits[i] == y_bits[i]:
				xorv += '0'
			else:
				xorv += '1'

	else:
		print("INTERNAL ERROR: bitXOR() requires x_bits and y_bits be the same size.")
		exit(1)

	return xorv


## WORKS
def bitShiftLeft(bit_str, shift_amount):
	# test_bits:  '00101011110100110000100111110000'
	# test_amnt:   7
	# result:     'e984f815'
	register = []
	for i in range(len(bit_str)):
		register.append(bit_str[i])

	for i in range(shift_amount):
		bit = register.pop(0)
		register.append(bit)

	shift_str = ""
	for i in range(len(register)):
		shift_str += register[i]

	return shift_str


## WORKS
def functionF(x_bits, y_bits, z_bits):
	# test_x:  '10001001101010111100110111101111'
	# test_y:  '11111110110111001011101010011000'
	# test_z:  '01110110010101000011001000010000'
	# result:  'fedcba98'
	xy = bitAnd(x_bits, y_bits)
	nx = bitNot(x_bits)
	nxz = bitAnd(nx, z_bits)
	f = bitOr(xy, nxz)

	return f


## ??
def functionG(x_bits, y_bits, z_bits):
	# test_x:  '00101100001101001101111110100010'
	# test_y:  '11011110000101100111001110111110'
	# test_z:  '01001011100101110110001010000010'
	# result:  '1c1453be'
	xz = bitAnd(x_bits, z_bits)
	nz = bitNot(z_bits)
	ynz = bitAnd(y_bits, nz)
	g = bitOr(xz, ynz)

	return g


## WORKS
def functionH(x_bits, y_bits, z_bits):
	# test_x:  '11010101000001110001001101100111'
	# test_y:  '11000000010110001010110111100010'
	# test_z:  '01100011110001100000001111010111'
	# result:  '7699bd52'
	x_xor_y = bitXOR(x_bits, y_bits)
	h = bitXOR(x_xor_y, z_bits)

	return h


## WORKS
def functionI(x_bits, y_bits, z_bits):
	# test_x:  '01111101010100000010000001100011'
	# test_y:  '10001011001111010111000101011101'
	# test_z:  '00011101111000111010011100111001'
	# result:  'f46109ba'
	nz = bitNot(z_bits)
	xvnz = bitOr(x_bits, nz)
	i = bitXOR(y_bits, xvnz)

	return i



## WORKS (1/3)
def padMessage(message_bitstr):
	# test_bstr:  '01010100011010000110010101111001001000000110000101110010011001010010000001100100011001010111010001100101011100100110110101101001011011100110100101110011011101000110100101100011'
	# result:     '01010100011010000110010101111001001000000110000101110010011001010010000001100100011001010111010001100101011100100110110101101001011011100110100101110011011101000110100101100011100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010110000'
	message_len = len(message_bitstr)
	padded = ""

	if message_len < 447:
		padded = f"{message_bitstr}"
		padded += '1'
		while(len(padded) < 448):
			padded += '0'
		padded += getMessageLengthBits(message_bitstr)

	elif 447 <= message_len and message_len < 512:
		temp = ""
		counter = 0
		for i in range(message_len):
			if counter == 447:
				size_bits = getMessageLengthBits(temp)
				temp += '1'
				temp += size_bits
				padded += temp

				temp = ""
				counter = 0
			else:
				temp += message_bitstr[i]
				counter += 1

		while 0 < counter and counter < 447:
			temp += '0'
			counter += 1

		if temp != "":
			size_temp = getMessageLengthBits(temp)
			temp += '1'
			temp += size_temp
			padded += temp

	else:
		pass

	return padded


## WORKS
def toBlocks(padded_bitstr):
	blocks = []

	block = ""
	count = 0
	for i in range(len(padded_bitstr)):
		block += padded_bitstr[i]
		count += 1

		if count == 512:
			blocks.append(block)
			block = ""
			count = 0
	
	return blocks


## WORKS
def toWords(block_bitstr):
	words = []

	word = ""
	count = 0
	for i in range(len(block_bitstr)):
		word += block_bitstr[i]
		count += 1

		if count == 32:
			words.append(word)
			word = ""
			count = 0

	return words



def md5Hash(message_bitstr):
	# test_m:  '01010100011010000110010101111001001000000110000101110010011001010010000001100100011001010111010001100101011100100110110101101001011011100110100101110011011101000110100101100011'
	# result:  '23db6982caef9e9152f1a5b2589e6ca3'
	a0 = "01100111010001010010001100000001"
	b0 = "11101111110011011010101110001001"
	c0 = "10011000101110101101110011111110"
	d0 = "00010000001100100101010001110110"

	t_array = [
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

	s_array = [
		7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
		5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
		4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
		6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21
	]

	# pad message and break into blocks
	padded_msg = padMessage(message_bitstr)
	blocks = toBlocks(padded_msg)

	for block in blocks:
		a = a0
		b = b0
		c = c0
		d = d0
		m_array = toWords(block)

		for i in range(len(t_array)):
			f_bits = ""
			g = 0

			if (0 <= i) and (i < 16):
				f_bits = functionF(b, c, d)
				g = i
			elif (16 <= i) and (i < 32):
				f_bits = functionG(b, c, d)
				g = ((5 * i) + 1) % 16

			elif (32 <= i) and (i < 48):
				f_bits = functionH(b, c, d)
				g = ((3 * i) + 5) % 16

			else:
				f_bits = functionI(b, c, d)
				g = (7 * i) % 16

			fsum = modularAddition(f_bits, a)
			fsum = modularAddition(fsum, t_array[i])
			fsum = modularAddition(fsum, m_array[g])
			f_bits = fsum

			rotation = bitShiftLeft(f_bits, s_array[i])
			a = d
			d = c
			c = b
			b = modularAddition(b, rotation)

		a0 = modularAddition(a0, a)
		b0 = modularAddition(b0, b)
		c0 = modularAddition(c0, c)
		d0 = modularAddition(d0, d)

	digest = f"{a0}{b0}{c0}{d0}"
	return digest
