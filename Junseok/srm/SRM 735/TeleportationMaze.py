# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect


class TeleportationMaze:

    def pathLength(self, a, r1, c1, r2, c2):
        n = len(a)
        m = len(a[0])
        d = [[99999] * m for _ in range(n)]
        direction = ((-1, 0), (0, 1), (1, 0), (0, -1))

        q = [(r1, c1, 0)]

        def move(cur_r, cur_c, w):
            for r_dir, c_dir in direction:
                r, c = cur_r + r_dir, cur_c + c_dir
                while 0 <= r < n and 0 <= c < m and a[r][c] == '#':
                    r += r_dir
                    c += c_dir

                if 0 <= r < n and 0 <= c < m:
                    if r == cur_r + r_dir and c == cur_c + c_dir:
                        q.append((r, c, w + 1))
                    else:
                        q.append((r, c, w + 2))

        while q:
            cur_r, cur_c, w = q.pop(0)

            if 0 <= cur_r < n and 0 <= cur_c < m:
                if a[cur_r][cur_c] == '.' and w < d[cur_r][cur_c]:

                    d[cur_r][cur_c] = w
                    move(cur_r, cur_c, w)

        return d[r2][c2] if d[r2][c2] < 99999 else -1

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

def do_test(a, r1, c1, r2, c2, __expected):
    startTime = time.time()
    instance = TeleportationMaze()
    exception = None
    try:
        __result = instance.pathLength(a, r1, c1, r2, c2);
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
    sys.stdout.write("TeleportationMaze (600 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("TeleportationMaze.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            a = []
            for i in range(0, int(f.readline())):
                a.append(f.readline().rstrip())
            a = tuple(a)
            r1 = int(f.readline().rstrip())
            c1 = int(f.readline().rstrip())
            r2 = int(f.readline().rstrip())
            c2 = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(a, r1, c1, r2, c2, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1531362815
    PT, TT = (T / 60.0, 75.0)
    points = 600 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
