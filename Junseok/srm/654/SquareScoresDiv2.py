# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class SquareScoresDiv2:
    def getscore(self, s):
        prev_ch = None
        same_cnt = 0
        total = 0

        for cur_ch in s:
            if prev_ch == cur_ch:
                same_cnt += 1
            else:
                same_cnt = 1

            total += same_cnt

            prev_ch = cur_ch
                
        return total
