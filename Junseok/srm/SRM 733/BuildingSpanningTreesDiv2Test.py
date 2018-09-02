import unittest

from BuildingSpanningTreesDiv2 import BuildingSpanningTreesDiv2


class BuildingSpanningTreesDiv2Test(unittest.TestCase):

    def setUp(self):
        self.obj = BuildingSpanningTreesDiv2()

    def test_merge_group(self):
        group = [0,1,2,3,4]
        expect = [0,1,2,3,3]
        self.obj.merge_group(group, 3, 4)
        self.assertEqual(group, expect)

        group = [0,1,1,3,3]
        expect = [0,1,1,0,0]
        self.obj.merge_group(group, 0, 3)
        self.assertEqual(group, expect)

    def test_get_cnt(self):
        group = [0,1,1,3,3]
        expect = [1,2,2]
        result = self.obj.get_cnt(group)
        self.assertEqual(result, expect)

        group = [1,1,1,3,3]
        expect = [3,2]
        result = self.obj.get_cnt(group)
        self.assertEqual(result, expect)
