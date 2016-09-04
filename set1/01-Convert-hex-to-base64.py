#!/usr/bin/env python

import base64

def string2binary(s):
	return s.decode("hex")
	
def hex2base64(s):
	b = string2binary(s)
	result = base64.b64encode(b)
	return result

assert hex2base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


