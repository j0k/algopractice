def mini(a,i,b,j):
    return (a,i) if a<=b else (b,j)

def maxi(a,i,b,j):
    return (a,i) if a>=b else (b,j)


def maxseq(a):
    if len(a) <= 1:
        return 0

    m,M,el = a[0],a[0],a[0]
    mi,Mi  = 0, 0

    order = True
    changed = True
    d = 0

    A = [d,[M,m], [Mi,mi], a]
    for (i,e) in enumerate(a):
        if e == el:
            continue
        elif (e > el) ^ (not order):
            m,mi = el,i-1
            M,Mi = el,i-1

        m,mi = mini(e,i, m,mi)
        M,Mi = maxi(e,i, M,Mi)

        if M - m > A[0]:
            l,r = min(mi,Mi), max(mi,Mi)
            A = [M-m, [M,m], [Mi,mi], a[l:r+1]]

        el = e
        order = e>el

    return A

import random

A = range(31)
A = random.sample(A, len(A))

print(A)
print(maxseq(A))
