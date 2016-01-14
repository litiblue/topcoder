from itertools import permutations

class FourStrings(object):
    def shortestLength(self, *args):
        def concat(a, b):
            if b in a:
                return a
            for k in xrange(min(len(a), len(b)), -1, -1):
                if a[-k:] == b[:k]:
                    return a + b[k:]
            return a + b
            
        return min(len(reduce(concat, perm)) for perm in permutations(args))
