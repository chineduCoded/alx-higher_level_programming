#!/usr/bin/python3
for char in range(26):
	    if char != 5 and char != 17:
		            print("{:s}".format(chr(char + ord("a"))), end="")
