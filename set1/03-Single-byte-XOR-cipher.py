#!/usr/bin/env python

def hexString2string(s):
	return s.decode("hex")
	
def string2hexString(b):
	return b.encode("hex")

def charIntXor(a, b):
	return chr(ord(a) ^ b)

def decodeStringWithSingleInt(b, x):
	# enough spaces?
	c = charIntXor(' ', x)
	if b.count(c) < len(b) / 8:
		return None

	# decode
	result = ""
	for i in range(0, len(b)):
		c = charIntXor(b[i], x)

		# illegal char?
		if c < ' ' or c > '~':
			if ord(c) != 10 and ord(c) != 13:
				return None
		result += c
		
	# found a legal string!
	return result

def solveDecodeStringWithSingleInt(s):
	b = hexString2string(s)
	for i in range(0, 255):
		s = decodeStringWithSingleInt(b, i)
		if s != None:
			print s

solveDecodeStringWithSingleInt("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

