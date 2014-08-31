import sys
from collections import defaultdict

class Egalitarianism3Easy(object):
	
	def maxCities(self, n, a, b, len):
		d = [[sys.maxint] * (n+1)] * (n+1)

		for i in range(n-1):
			d[a[i]][b[i]] = d[b[i]][a[i]] = len[i]

		for k in range(1,n+1):
			for i in range(1,n+1):
				for j in range(1,n+1):
					d[i][j] = min(d[i][j], d[i][k]+d[k][j])

		max_cnt = -999
		for i in range(1,n+1):
			for j in range(i,n+1):
				cnt = 1
				for k in range(j+1, n+1):
					if d[i][j] == d[i][k]:
						cnt += 1
				max_cnt = max(max_cnt, cnt)

		return max_cnt

if __name__ == '__main__':
	egal = Egaliterianism3Easy()	
	#print egal.maxCities(4, [1,1,1], [2,3,4], [1,1,1])
	#print egal.maxCities(6, [1,2,3,2,3], [2,3,4,5,6], [2,1,3,2,3])
	#print egal.maxCities(10, [1,1,1,1,1,1,1,1,1,1], [2,3,4,5,6,7,8,9,10], \
	#[1000,1000,1000,1000,1000,1000,1000,1000,1000])
	#print egal.maxCities(2, [1], [2], [3])
	print egal.maxCities(1, [], [], [])
