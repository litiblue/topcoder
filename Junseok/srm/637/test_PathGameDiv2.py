import unittest
import PathGameDiv2

class test_PathGameDiv2(unittest.TestCase):
	
	def setUp(self):
		self.pathGameDiv2 = PathGameDiv2.PathGameDiv2()

	def test_0(self):
		in_data = ["....#.##.....#...........","..#......#.......#..#...."]
		self.assertEqual(self.pathGameDiv2.calc(in_data), 13)
	
	def test_1(self):
		in_data = ["#","."]
		self.assertEqual(self.pathGameDiv2.calc(in_data), 0)

if __name__ == '__main__':
	unittest.main()
