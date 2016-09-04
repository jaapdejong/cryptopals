#!/usr/bin/env python

def hexString2string(s):
	return s.decode("hex")
	
def string2hexString(b):
	return b.encode("hex")

def stringStringXor(s1, s2):
	result = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1, s2))
	return string2hexString(result)


s1 = hexString2string("1c0111001f010100061a024b53535009181c")
s2 = hexString2string("686974207468652062756c6c277320657965")
assert stringStringXor(s1, s2) == "746865206b696420646f6e277420706c6179"

