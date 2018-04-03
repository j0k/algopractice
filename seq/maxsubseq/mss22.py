import random

class Elem:
    def __init__(_, e, i):
        _.e = e
        _.i = i

    @staticmethod
    def I(a,i):
        return Elem(a[i],i)

def maxe(a,b):
    return a if (a.e >= b.e) else b
def mine(a,b):
    return a if (a.e <= b.e) else b

def mmseq(a):
    if len(a)<=1:
        return 0

    m = Elem(a[0], 0)
    m, M, el = map(lambda i: Elem.I(a,i), [0,0,0])

    t = True
    d = 0

    order = True
    for (i,e) in enumerate(a):
        E = Elem(e,i)
        if E.e == el.e:
            continue
        changed = (E.e > el.e) and order
        order   = (E.e > el.e)

        if changed:
            m,M = el,el

        m,M = mine(E,m), maxe(E,M)
        el = E

        if M.e - m.e > d:
            d = M.e - m.e

    return d

A = range(28)
A = random.sample(A, len(A))

print(A)
print(mmseq(A))

# aml notes:
# it will be cool to have 2d visualization to get fast understanding
# as a first step we can
#   - change SIZE of Symbols
#   - use very short term notation
#   - use colorizing
