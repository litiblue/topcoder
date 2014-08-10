from collections import defaultdict

class BracketExpressions(object):

    def ifPossible(self, expression):
        self.d = defaultdict(lambda: defaultdict(lambda: None))

        def isPair(left_ch, right_ch):
            if left_ch == '[':
                return right_ch in "X]"
            elif left_ch == '(':
                return right_ch in 'X)'
            elif left_ch == '{':
                return right_ch in 'X}'
            elif left_ch == 'X':
                return right_ch in 'X])}'
            else:
                return False

        def recur(expression, left, right):
            if self.d[left][right] != None:
                return self.d[left][right]

            res = False

            if left+1 == right:
                if isPair(expression[left], expression[right]):
                    res = True
            else:
                if isPair(expression[left], expression[right]) and recur(expression, left+1, right-1):
                    res = True
                else:
                    for m in xrange(left+1, right-1, 2):
                        if recur(expression, left, m) and recur(expression, m+1, right):
                            res = True
                            break

            self.d[left][right] = res
            return res

        if len(expression) % 2 == 1:
            return "impossible"

        if recur(expression, 0, len(expression)-1):
            return "possible"
        else:
            return "impossible"

def main():
    bracketExpressions = BracketExpressions()
    print bracketExpressions.ifPossible("([]X()[()]XX}[])X{{}}]")

if __name__ == "__main__":
    main()
