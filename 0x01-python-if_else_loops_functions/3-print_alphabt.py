#!/usr/bin/python3
for letter in range(97, 123):
    if chr(letter) is 'q' and chr(letter) is not 'e':
        print("{}".format(chr(letter)), end="")
