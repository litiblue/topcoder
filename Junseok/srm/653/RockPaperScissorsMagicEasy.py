# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class RockPaperScissorsMagicEasy:
    def count(self, card, score):
        if score > len(card): return 0
        C = lambda n, r:\
            math.factorial(n) / math.factorial(n-r) / math.factorial(r)

        MOD = 10**9+7
        win_cnt = C(len(card), score) % MOD
        lose_cnt = (math.pow(2,(len(card)-score))) % MOD

        return (win_cnt * lose_cnt) % MOD
