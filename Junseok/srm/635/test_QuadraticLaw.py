import unittest
import QuadraticLaw

class TestQuadraticLaw(unittest.TestCase):

    def setUp(self):
        self.q = QuadraticLaw.QuadraticLaw()

    def test_0(self):
        self.assertEqual(0, self.q.getTime(1))

    def test_1(self):
        self.assertEqual(1, self.q.getTime(2))

    def test_2(self):
        self.assertEqual(1, self.q.getTime(5))

    def test_3(self):
        self.assertEqual(2, self.q.getTime(6))

    def test_4(self):
        self.assertEqual(2, self.q.getTime(7))

    def test_5(self):
        self.assertEqual(38, self.q.getTime(1482))

    def test_6(self):
        self.assertEqual(999999999, self.q.getTime(1000000000000000000))

    def test_7(self):
        self.assertEqual(178770270, self.q.getTime(31958809614643170))

    def test_8(self):
        self.assertEqual(999999998, self.q.getTime(999999998999999999))

if __name__ == '__main__':
    unittest.main()
