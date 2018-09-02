# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class BridgeBuildingDiv2:

    def find_min_diameter(self, a, b, K, edge_list, edge_n):
        graph_n = edge_n * 2

        # init graph
        g = [[0 if i == j else 99999 for i in xrange(graph_n)] for j in xrange(graph_n)]

        # top
        for idx, dist in enumerate(a):
            g[idx][idx+1] = g[idx+1][idx] = dist

        # bottom
        for idx, dist in enumerate(b):
            g[idx+edge_n][idx+edge_n+1] = g[idx+edge_n+1][idx-edge_n] = dist

        # vertical
        for idx, value in enumerate(edge_list):
            if value == 1:
                g[idx][idx+edge_n] = g[idx+edge_n][idx] = 0

        # floyd
        for k in xrange(0, graph_n):
            for i in xrange(0, graph_n):
                for j in xrange(0, graph_n):
                    if g[i][k] + g[k][j] < g[i][j]:
                        g[i][j] = g[i][k] + g[k][j]

        # find_max_value
        max_value = -99999
        for i in xrange(0, graph_n):
            for j in xrange(0, graph_n):
                max_value = max(max_value, g[i][j])

        return max_value

    def minDiameter(self, a, b, K):
        edge_n = len(a) + 1
        s = 0
        res = 99999

        while s < (1 << edge_n):
            edge_list = []
            for i in xrange(edge_n):
                edge_list.append((s & (1 << i)) >> i)

            if edge_list.count(1) == K:
                value = self.find_min_diameter(a, b, K, edge_list, edge_n)
                res = min(res, value)

            s += 1
        return res


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

def do_test(a, b, K, __expected):
    startTime = time.time()
    instance = BridgeBuildingDiv2()
    exception = None
    try:
        __result = instance.minDiameter(a, b, K);
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
    sys.stdout.write("BridgeBuildingDiv2 (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("BridgeBuildingDiv2.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            a = []
            for i in range(0, int(f.readline())):
                a.append(int(f.readline().rstrip()))
            a = tuple(a)
            b = []
            for i in range(0, int(f.readline())):
                b.append(int(f.readline().rstrip()))
            b = tuple(b)
            K = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(a, b, K, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1438846596
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
