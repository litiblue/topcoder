# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect


def dfs(graph, start, end):
    stack = [(start, 0)]
    visited = []

    while True:
        node, w = stack.pop()
        if node == end:
            return w
        elif node in visited:
            continue
        else:
            visited.append(node)
            stack.extend(map(lambda nnw: (nnw[0], w + nnw[1]), graph[node]))
    return None

class LuckyCycle:
    def getEdge(self, edge1, edge2, weight):
        #edge1 = [1,3,2,4]
        #edge2 = [2,2,4,5]
        #weight = [4,7,4,7]
        n = len(edge1) + 1
        tw = map(lambda w: 1 if w == 7 else -1, weight)
        graph = collections.defaultdict(list)
        for node1, node2, w in zip(edge1, edge2, tw):
            graph[node1].append((node2, w))
            graph[node2].append((node1, w))

        for start in xrange(1, n+1):
            for end in xrange(start+1, n+1):
                value = dfs(graph, start, end)
                if value and abs(value) == 1 and end not in map(lambda x: x[0], graph[start]):
                    return (start, end, 4 if value == 1 else 7)
        return ()
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

def do_test(edge1, edge2, weight, __expected):
    startTime = time.time()
    instance = LuckyCycle()
    exception = None
    try:
        __result = instance.getEdge(edge1, edge2, weight);
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
    sys.stdout.write("LuckyCycle (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("LuckyCycle.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            edge1 = []
            for i in range(0, int(f.readline())):
                edge1.append(int(f.readline().rstrip()))
            edge1 = tuple(edge1)
            edge2 = []
            for i in range(0, int(f.readline())):
                edge2.append(int(f.readline().rstrip()))
            edge2 = tuple(edge2)
            weight = []
            for i in range(0, int(f.readline())):
                weight.append(int(f.readline().rstrip()))
            weight = tuple(weight)
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(int(f.readline().rstrip()))
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(edge1, edge2, weight, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1439891670
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
