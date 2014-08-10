#!/usr/bin/env python

import sys

r_max = 8
c_max = 8

class BishopMove:

    def moves(self, r1, c1, r2, c2, step, dir):

        if r1==r2 and c1==c2:   #same position
            if(step==0):
                return 0
            else:
                return step

        if(step > 1):   return -1

        mv_r_max = r_max - 1 - r1
        mv_r_min = r1
        mv_c_max = c_max - 1 - c1
        mv_c_min = c1
        if(mv_r_max < mv_c_max):    dir1_max = mv_r_max
        else:   dir1_max = mv_c_max

        if(mv_r_min < mv_c_min):    dir2_max = mv_r_min
        else:   dir2_max = mv_c_min

        if(mv_r_max < mv_c_min):    dir3_max = mv_r_max
        else:   dir3_max = mv_c_min

        if(mv_r_min < mv_c_max):    dir4_max = mv_r_min
        else:   dir4_max = mv_c_max

        if dir!=1 and dir!=2:
            for num in range(1,dir1_max+1):
                result = self.moves(r1+num, c1+num, r2, c2, step+1, 1)
                if(result!=-1): return result
            for num in range(1,dir2_max+1):
                result = self.moves(r1-num, c1-num, r2, c2, step+1, 2)
                if(result!=-1): return result
        if dir!=3 and dir!=4:
            for num in range(1,dir3_max+1):
                result = self.moves(r1+num, c1-num, r2, c2, step+1, 3)
                if(result!=-1): return result
            for num in range(1,dir4_max+1):
                result = self.moves(r1-num, c1+num, r2, c2, step+1, 4)
                if(result!=-1): return result

        return -1

    def howManyMoves(self, r1, c1, r2, c2):
        return self.moves(r1,c1,r2,c2,0,0)
