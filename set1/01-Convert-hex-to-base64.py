#!/usr/bin/env python

import base64

def encodeBase64(s):
	return base64.b64encode(s)

def hexString2string(s):
	return s.decode("hex")

h = hexString2string("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
assert encodeBase64(h) == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

