class BoardEscapeDiv2(object):
    def findWinner(self, a, k):
        def dfs(i, j, k):
            res = d[i][j][k]
            if res == -1:
                if a[i][j] == 'E' or k == 0:
                    res = 0
                else:
                    res = 0
                    for di, dj in ((-1,0),(0,1),(1,0),(0,-1)):
                        ni, nj = i+di, j+dj
                        if ni >= 0 and nj >= 0 and ni < n and nj < m and a[ni][nj] != '#':
                            if dfs(ni, nj, k-1) == 0:
                                res = 1
                d[i][j][k] = res
            return res
        
        n = len(a)
        m = len(a[0])
        d = [[[-1]*101 for _ in xrange(m)] for _ in xrange(n)]
        
        for i in xrange(n):
            for j in xrange(m):
                if a[i][j] == 'T':
                    si, sj = i, j
                    
        return 'Alice' if dfs(si, sj, k) == 1 else 'Bob'
