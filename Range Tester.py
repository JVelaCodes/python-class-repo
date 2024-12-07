# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:07:54 2024


fix out of bounds number error output

@author: jvela8217
"""
from random import randint

top = 100
bottom = 0

num = randint(bottom,top)
i = 9000000
iteration = 0
check = []

for i in range(0,101):
    num = randrange(0,101)
    if num not in check:
        check.append(num)
        print(f"{iteration}% completed successfully")
        
    if i == 0:
        print("range within bounds")
        
if False in check:
    for n in range(len(check)):
        if check[n] == False:
            print(f"range unsuccessful; missed {check[n]}")
else: print("range successfully hit all numbers")

if i != 0:
    print("range unsuccessful")
    print(f"number outside of bounds: {num}")