# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect


class BuildingSpanningTreesDiv2:

    def merge_group(self, group, first, second):
        target = group[second]
        for idx in range(len(group)):
            if group[idx] == target:
                group[idx] = group[first]

    def get_cnt(self, group):
        return collections.Counter(group).values()

    def getNumberOfSpanningTrees(self, n, x, y):
        self.n = n
        group = range(self.n)
        for idx in range(n-3):
            self.merge_group(group, x[idx]-1, y[idx]-1)

        cnt = self.get_cnt(group)
        def mod(a, b):
            return a * b % 987654323

        if len(cnt) == 3:
            return mod(mod(cnt[2], (cnt[0] + cnt[1])), mod(cnt[0], cnt[1])) + \
                   mod(mod(cnt[0], cnt[2]), mod(cnt[1], cnt[2]))
        else:
            return 0

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(n, x, y, __expected):
    startTime = time.time()
    instance = BuildingSpanningTreesDiv2()
    exception = None
    try:
        __result = instance.getNumberOfSpanningTrees(n, x, y);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("BuildingSpanningTreesDiv2 (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("BuildingSpanningTreesDiv2.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            n = int(f.readline().rstrip())
            x = []
            for i in range(0, int(f.readline())):
                x.append(int(f.readline().rstrip()))
            x = tuple(x)
            y = []
            for i in range(0, int(f.readline())):
                y.append(int(f.readline().rstrip()))
            y = tuple(y)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            #if not (cases - 1 == 8):
            #    continue

            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(n, x, y, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1531971569
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
