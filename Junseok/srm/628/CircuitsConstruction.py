class CircuitsConstruction(object):

    def maximizeResistance(self, circuit, conductors):
        s = []
        for ch in circuit[::-1]:
            if ch == 'X':
                s.append(1)
            else:
                p = s.pop()
                q = s.pop()
                if ch == 'A':
                    s.append(p + q)
                else:
                    s.append(max([p,q]))

        cnt = s.pop()
        return sum(sorted(conductors, reverse=True)[:cnt])
