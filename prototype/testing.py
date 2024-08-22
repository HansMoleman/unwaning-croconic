#!/usr/bin/python3

### testing.py
#
#
##

from hashing import md5Hash, binaryToHex
from utf8encoding import binaryToString


tbit_str = "010101000110100001101001011100110010000001101001011100110010000001100001001000000111001101100001011011010111000001101100011001010010000001110011011101000111001001101001011011100110011100100000011001100110111101110010001000000111010001100101011100110111010001101001011011100110011100100000010011010100010000110101001000000110100001100001011100110110100001101001011011100110011100101110"
hash_bit = md5Hash(tbit_str)

print(f"original message:\n{binaryToString(tbit_str)}\n")
print(f"digest:  {binaryToHex(hash_bit)}")
