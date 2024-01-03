#!/usr/bin/python3
for alphabet in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    alphabet = alphabet.lower()
    if alphabet != "e" and alphabet != "q":
        print(alphabet.format(), end="")
