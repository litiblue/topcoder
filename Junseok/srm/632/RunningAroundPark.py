class RunningAroundPark(object):

	def numberOfLap(self, N, d):
		a = list(d)
		
		cur = a.pop(0)
		
		lap = 0
		while True:
			lap += 1
			for i in range(1,N+1):
				if i == cur:
					try:	
						cur = a.pop(0)
					except:
						return lap
			
if __name__ == '__main__':
	r = RunningAroundPark()
	print r.numberOfLap(3, (1,2,3))
	print r.numberOfLap(24, (6,6))
	print r.numberOfLap(3, (3,2,1))
	print r.numberOfLap(50, (1,3,5,7,9,2,4,6,8,10))
