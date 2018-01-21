#!/bin/python

f = open("textfile", "r")

# print first word per line
while True:
    l = f.readline()
    if l == "":
        break

    firstword = l.split(" ")[0].strip()

    if firstword.isalpha():
        print(firstword)

    print("*************")
