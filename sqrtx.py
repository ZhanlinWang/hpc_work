#!/bin/python
from numpy import *
x = 2.
s = 1.
for k in range(60):
	s = 0.5 * (s + x/s)
print(s)
