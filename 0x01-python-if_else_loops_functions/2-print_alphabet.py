#!/usr/bin/python3
alphabets = ""
for letters in range(ord("a"), ord("z") + 1):
	alphabets += (chr(letters))
letter = "".join(alphabets)
print("{}".format(letter))
