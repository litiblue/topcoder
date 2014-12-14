class PathGameDiv2(object):

	def calc(self, a):
		MIN = -99999
		
		if a[0][0] == '.' and a[1][0] == '.':
			prev_d_none, prev_d_zero, prev_d_one = 0, 1, 1
		elif a[0][0] == '#' and a[1][0] == '.':
			prev_d_none, prev_d_zero, prev_d_one = MIN, 0, MIN
		elif a[0][0] == '.' and a[1][0] == '#':
			prev_d_none, prev_d_zero, prev_d_one = MIN, MIN, 0 
		
		for i in xrange(1, len(a[0])):
			if a[0][i] == '#' or a[1][i] == '#':
				d_none = MIN
			else:
				d_none = max(prev_d_none, prev_d_zero, prev_d_one)
		
			if a[0][i] == '.' and a[1][i] == '#':
				d_zero = MIN
			else:
				d_zero = max(prev_d_none, prev_d_zero) + int(a[0][i] == '.')
		
			if a[0][i] == '#' and a[1][i] == '.':
				d_one = MIN
			else:	
				d_one = max(prev_d_none, prev_d_one) + int(a[1][i] == '.')

			prev_d_none, prev_d_zero, prev_d_one = d_none, d_zero, d_one
		
		return max(prev_d_none, prev_d_zero, prev_d_one)
