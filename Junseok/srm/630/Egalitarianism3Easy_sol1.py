import sys

class Egalitarianism3Easy(object):
	
	def maxCities(self, n, a, b, lens):
		INF = 50000000
		d = [[INF for x in range(n)] for x in range(n)]
		for i in range(n-1):	
			d[ a[i]-1 ][ b[i]-1 ] = lens[i]
			d[ b[i]-1 ][ a[i]-1 ] = lens[i]

		for k in range(n):
			for i in range(n):
				for j in range(n):
					d[i][j] = min(d[i][j], d[i][k] + d[k][j])

		res = 0
		for mask in range(0, (1<<n)):
			x = -1
			c = 0
			different = False
			for i in range(n):
				if mask & (1<<i):
					c += 1
					for j in range(n):
						if i != j and mask & (1<<j):
							if x == -1:
								x = d[i][j]
							elif x != d[i][j]:
								different = True

			if not different:
				res = max(res, c)

		return res

if __name__ == '__main__':
	egal = Egalitarianism3Easy()	
	print egal.maxCities(4, [1,1,1], [2,3,4], [1,1,1]) == 3
	print egal.maxCities(6, [1,2,3,2,3], [2,3,4,5,6], [2,1,3,2,3]) == 3
	print egal.maxCities(10, [1,1,1,1,1,1,1,1,1,1], [2,3,4,5,6,7,8,9,10], \
	[1000,1000,1000,1000,1000,1000,1000,1000,1000]) == 9
	print egal.maxCities(2, [1], [2], [3]) == 2
	print egal.maxCities(1, [], [], []) == 1
	print egal.maxCities(5, [3,4,2,5], [1,2,3,4], [446,446,446,443]) == 2
