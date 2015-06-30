# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class BichromeBoard:
    def ableToDraw(self, board):
        wchk = bchk = 0
        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c == 'W': wchk |= 1<<((i+j)%2)
                if c == 'B': bchk |= 1<<((i+j)%2)

        if wchk == 3 or bchk == 3: return 'Impossible'
        elif wchk & bchk != 0: return 'Impossible'
        return 'Possible'
