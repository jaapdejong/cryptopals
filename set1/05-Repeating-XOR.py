#!/usr/bin/python

def hexString2string(s):
	return s.decode("hex")
	
def string2hexString(b):
	return b.encode("hex")

def charIntXor(a, b):
	return chr(ord(a) ^ b)

def encodeXor(s, k):
	result = ""
	for i in range(0, len(s)):
		a = s[i]
		x = ord(k[i % len(k)])
		c = charIntXor(a, x)
		result += c
	return string2hexString(result)

assert encodeXor("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal", "ICE") == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

