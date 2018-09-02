import unittest

from TheSquareCityDiv2 import TheSquareCityDiv2

class TheSquareCityDiv2Test(unittest.TestCase):

    def setUp(self):
        self.obj = TheSquareCityDiv2()

    def test_can_move(self):
        self.obj.r = 2
        self.obj.n = 3
        self.assertTrue(self.obj.can_move(5, 1))
        self.assertTrue(self.obj.can_move(5, 2))
        self.assertTrue(self.obj.can_move(5, 3))
        self.assertTrue(self.obj.can_move(5, 4))
        self.assertTrue(self.obj.can_move(5, 5))
        self.assertTrue(self.obj.can_move(5, 7))
        self.assertTrue(self.obj.can_move(5, 8))
        self.assertFalse(self.obj.can_move(5, 0))
        self.assertFalse(self.obj.can_move(5, 6))

    def test_all_move(self):
        self.obj.r = 3
        self.obj.n = 5
        self.obj.t = [0] * 25
        expect = ((3,7,8,9,11,12,13,14,15,16,17,18,19,21,22,23,24))
        result = tuple(self.obj.all_move(18))

        self.assertEqual(result, expect)

    def test_get_warmest(self):
        self.obj.r = 2
        self.obj.t = [5,2,1,6,4,3,9,8,7]
        self.obj.n = 3

        expect = [6,7,8,6,6,7,6,6,6]
        result = self.obj.get_warmest()
        self.assertEqual(result, expect)

    def test_get_end(self):
        self.obj.r = 1
        self.obj.n = 3
        self.obj.t = [9,1,6,5,3,2,7,4,8]

        warmest = [7,2,2,1,1,4,4,7,7]
        expect = [7,2,2,2,2,2,2,7,7]
        result = self.obj.get_final(warmest)
        self.assertEqual(result, expect)

    def test_calc(self):
        final = [7,2,2,2,2,2,2,7,7]
        houses, max_cnt = self.obj.calc(final)
        self.assertEqual((houses, max_cnt), (2, 6))

    def test_find(self):
        pass

if __name__ == '__main__':
    unittest.main()
