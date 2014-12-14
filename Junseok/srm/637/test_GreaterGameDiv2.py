import unittest
import GreaterGameDiv2

class GreaterGameDiv2Test(unittest.TestCase):

	def setUp(self):
		self.createGameDiv2 = GreaterGameDiv2.GreaterGameDiv2()

	def test_0(self):
		print 'aaa'

	def test_1(self):
		exptd = 6
		res = self.createGameDiv2.calc([3,5,9,16,14,20,15,17,13,2], [6,18,1,8,7,10,11,19,12,4])
		self.assertEqual(res, exptd)

if __name__ == '__main__':
	unittest.main()
