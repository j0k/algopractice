import random

class Elem:
    def __init__(_, e, i):
        _.e = e
        _.i = i

def maxi(e1, e2):
    return e1 if e1.e >= e2.e else e2

def mini(e1, e2):
    return e1 if e1.e <= e2.e else e2

def maxseq(a):
    if len(a)<=1:
        return 0

    m, M, El = Elem(a[0], 0), Elem(a[0], 0), Elem(a[0], 0)
    t = True
    d = 0

    A = []
    for i,e in enumerate(a):
        E = Elem(e,i)
        if E.e == El.e:
            continue
        elif (t and E.e > El.e) or (not t and E.e < El.e):
            m, M = mini(E,m), maxi(E, M)
        else:
            t = not t
            m, M = mini(E, El), maxi(E, El)
        El = E

        if M.e - m.e > d:
            d = M.e - m.e
            l,r = min(M.i, m.i), max(M.i, m.i)
            A = [M, m, d, a[l:r+1]]

    return A



A = list(range(23))
A = random.sample(A, len(A))

print(A)
print(maxseq(A))
