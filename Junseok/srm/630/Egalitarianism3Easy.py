import sys
import pprint
from collections import defaultdict

class Egalitarianism3Easy(object):
	
	def maxCities(self, n, a, b, lens):
		
		d = defaultdict(defaultdict)
		for i in range(0,n+1):
			for j in range(0,n+1):
				d[i][j] = sys.maxint
		for i in range(1,n+1):
			d[i][i] = 0

		for i in range(n-1):
			d[a[i]][b[i]] = d[b[i]][a[i]] = lens[i]
		
		for k in range(1,n+1):
			for i in range(1,n+1):
				for j in range(1,n+1):
					d[i][j] = min(d[i][j], d[i][k]+d[k][j])

		def is_possible(group, new_node):
			dist = d[group[0]][group[1]]
			for each_node in group:
				if d[each_node][new_node] != dist:
					return False
			return True

		max_cnt = 1
		
		for i in range(1,n+1):
			for j in range(i+1,n+1):
				if d[i][j] != sys.maxint:
					group = [i, j]
					for k in range(j+1,n+1):
						if is_possible(group, k):
							group.append(k)
					max_cnt = max(max_cnt, len(group))

		return max_cnt

if __name__ == '__main__':
	egal = Egalitarianism3Easy()	
	print egal.maxCities(4, [1,1,1], [2,3,4], [1,1,1]) == 3
	print egal.maxCities(6, [1,2,3,2,3], [2,3,4,5,6], [2,1,3,2,3]) == 3
	print egal.maxCities(10, [1,1,1,1,1,1,1,1,1,1], [2,3,4,5,6,7,8,9,10], \
	[1000,1000,1000,1000,1000,1000,1000,1000,1000]) == 9
	print egal.maxCities(2, [1], [2], [3]) == 2
	print egal.maxCities(1, [], [], []) == 1
	print egal.maxCities(5, [3,4,2,5], [1,2,3,4], [446,446,446,443]) == 2
