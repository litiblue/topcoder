class BishopMove(object):

def howManyMoves(self, r1, c1, r2, c2):
    if (r1 + c1) % 2 != (r2 + c2) % 2:
        res  = -1
    else:
        res = 2
        if r1 + c1 == r2 + c2:
            res -= 1
        if r1 - c1 == r2 - c2:
            res -= 1

    return res
