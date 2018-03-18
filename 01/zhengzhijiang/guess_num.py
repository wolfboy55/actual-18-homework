#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random

i = 0
random_num = random.randint(0,100)
print (random_num)

while i < 5:
    input_num = raw_input('pls guess a num:')
    if int(input_num) == random_num:
        print ('Congratulations!!!')
        break
    i += 1

if 5 == i:
    print ('sb!!!')
