#!/usr/bin/env python

def string2binary(s):
	return s.decode("hex")
	
def binary2string(b):
	return b.encode("hex")

def xor(s1, s2):
	b1 = string2binary(s1)
	b2 = string2binary(s2)
	result = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(b1, b2))
	return binary2string(result)
    
assert xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965") == "746865206b696420646f6e277420706c6179"

