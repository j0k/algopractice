import random

class Elem:
    def __init__(_, e, i):
        _.e = e
        _.i = i

    @staticmethod
    def I(a,i):
        return Elem(a[i], i)

def maxi(a,b):
    return a if (a.e >= b.e) else b
def mini(a,b):
    return a if (a.e <= b.e) else b

def maxseq(a):
    if len(a) <= 1:
        return 0

    m, M, d, el = Elem.I(a, 0), Elem.I(a, 0), 0, Elem.I(a, 0)
    t = True

    for i,e_ in enumerate(a):
        e = Elem(e_,i)
        if e.e == el.e:
            continue
        elif (t and e.e > el.e) or (not t and e.e < el.e):
            m,M = mini(m,e), maxi(M,e)
        else:
            t = not t
            m,M = mini(el,e), maxi(el,e)

        if d < M.e - m.e:
            d = M.e - m.e
            l,r = min(m.i, M.i), max(m.i, M.i)
            A = {"dist":d, "min": m.e, "max": M.e, "inds": [m.i, M.i], "seq": a[l:r+1]}
        el = e

    return A


A = range(27)
A = random.sample(A, len(A))

print(A)
print(maxseq(A))
# AML free form
# e cmp cond => if true => c = cond
