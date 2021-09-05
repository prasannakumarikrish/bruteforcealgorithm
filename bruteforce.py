# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 08:46:36 2021

@author: PRASANNA
"""


import itertools, math
import os
Alphabet = ("Abdulkasim234560") # Add or remove whatevs you think will be in the password you're cracking (example, [symbols])
counter = 1
CharLength = 1
range_num = int(input("Enter range: "))
stopper = range_num + 1
filename = "bruteforce_%r.txt" % (range_num)
f = open(filename, 'a')
x = range_num
y = len(Alphabet)
amount = math.pow(y, x)
total_items = math.pow(y, x)
for CharLength in range(range_num, stopper):
    passwords = (itertools.product(Alphabet, repeat = CharLength))

for i in passwords:
    counter += 1
    percentage = (counter / total_items) * 100
    amount -= 1
    i = str(i)
    i = i.replace("[", "")
    i = i.replace("]", "")
    i = i.replace("'", "")
    i = i.replace(" ", "")
    i = i.replace(",", "")
    i = i.replace("(", "")
    i = i.replace(")", "")
    f.write(i)
	#f.write('\n')
    print("Password: %r\tPercentage: %r/100\tAmount left: %r" % (i, int(percentage), amount))
    if i == '0'* range_num:
        print("*Done")
        f.close()
        exit(0)
    else:
        pass