#!/bin/python

import sys


n = int(raw_input().strip())
if n%2==1:
    print('Weird')
elif n%2==0 and n>1 and n <=5:
    print('Not Weird')
elif n%2==0 and n>=6 and n <=20:
    print('Weird')
elif n%2==0 and n>=21:
    print('Not Weird')  
