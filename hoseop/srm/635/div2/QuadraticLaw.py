#!/usr/bin/env python

import math

class QuadraticLaw:
	def getTime(self,d):
		ex_t = long(math.sqrt(d))
		if ex_t*(ex_t+1) > d:	return ex_t-1
		else:	return ex_t
