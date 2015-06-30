# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class FoldingPaper2:
    def solve(self, W, H, A):

        def dist(init, target):
            if target > init: return 99999

            num = init
            cnt = 0
            while num > target:
                cnt += 1
                num = num / 2 + (num % 2 != 0)

            return cnt

        ans = 99999
        for first in range(1, A+1):
            if A % first == 0:
                second = A / first

                total = dist(W, first) + dist(H, second)
                ans = min(ans, total)

        return -1 if ans == 99999 else ans
