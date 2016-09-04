#!/usr/bin/env python

def hex2char(s):
	return s.decode("hex")
	
def char2hex(b):
	return b.encode("hex")

def xor(s1, s2):
	b1 = hex2char(s1)
	b2 = hex2char(s2)
	result = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(b1, b2))
	return char2hex(result)
    
assert xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965") == "746865206b696420646f6e277420706c6179"

