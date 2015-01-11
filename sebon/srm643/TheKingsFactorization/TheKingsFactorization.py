import unittest
import math

class TheKingsFactorization(object):
	def getPrimeNumber(self,start, remain):
		for i in xrange(start, int(math.sqrt(remain))+1):
			if remain%i == 0:
				return i
		return remain

	def getVector(self, N, primes):
		ans = []
		primes_len =  len(primes)
		remain = N
		
		for i in primes:
			while (remain%i == 0):
				remain =  remain/i
				ans.append(i)
		start = 1
		while True:
			if ((len(ans) +1)/2) ==len(primes):
				if (remain != 1) : ans.append(remain)
				return sorted(ans)
			else :
				start = self.getPrimeNumber(start+1, remain)
				ans.append(start)
				remain = remain/start

class TestFunctions(unittest.TestCase):
	def setUp(self):
		self.TheKingsFactorization = TheKingsFactorization()
		
	def test1(self):
		ans = self.TheKingsFactorization.getVector(12, [2, 3])
		self.assertEqual(ans, [2, 2, 3 ])
	
	def test2(self):
		ans = self.TheKingsFactorization.getVector(7, [7])
		self.assertEqual(ans, [7])
	
	def test3(self):
		ans = self.TheKingsFactorization.getVector(1764, [2, 3, 7])
		self.assertEqual(ans, [2, 2, 3, 3, 7, 7 ])
	
	def test4(self):
		ans = self.TheKingsFactorization.getVector(49, [7])
		self.assertEqual(ans, [7,7])
	
	def test5(self):
		ans = self.TheKingsFactorization.getVector(210, [2, 5])
		self.assertEqual(ans, [2, 3, 5, 7 ])
	
	def test6(self):
		ans = self.TheKingsFactorization.getVector(100000, [2, 2, 2, 5, 5])
		self.assertEqual(ans, [2, 2, 2, 2, 2, 5, 5, 5, 5, 5 ])

	def test7(self):
		ans = self.TheKingsFactorization.getVector(96799770, [2, 3, 37, 709])
		self.assertEqual(ans, [2, 3, 3, 5, 37, 41, 709])

	def test8(self):
		ans = self.TheKingsFactorization.getVector(500000006000000018, [2, 500000003])
		self.assertEqual(ans, [2, 500000003, 500000003])

	def test9(self):
		ans = self.TheKingsFactorization.getVector(576460752303423488, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
		self.assertEqual(ans, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
	#	1000000000000000000, {2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5}
	def test10(self):
		ans = self.TheKingsFactorization.getVector(1000000000000000000, [2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5])
		self.assertEqual(ans, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
		

if __name__ == '__main__':
    unittest.main()
