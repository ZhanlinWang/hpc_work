#!/bin/python
'''
Module for approximating sqrt.
More ...
'''
'Why not come here'
from numpy import *
x = 100.
def sqrt2(x, debug=False):
	'''
	more details
	'''
	s = 1.
	kmax = 100
	tol = 1.e-14
	for k in range(kmax):
		if debug:
			print "Before iteration %s, s = %20.15f" % (k,s)
		s0 = s
		s = 0.5 * (s + x/s)
		delta_s = s - s0
		if abs(delta_s/x) < tol:
			break
	if debug:
		print "After %s iteration, s=%20.15f" % (k+1,s)
	return s



