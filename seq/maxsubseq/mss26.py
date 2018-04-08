# 08.04.2018, boss 159 23:25

def minI(a,i,b,j):
    return (a,i) if a<b else (b,j)

def maxI(a,i,b,j):
    return (a,i) if a>b else (b,j)

def maxseq(a):
    if len(a) <= 1:
        return 0

    m,mi,M,Mi = a[0], 0, a[0], 0
    el = a[0]

    d = [0]
    order = True
    for (i,e ) in enumerate(a):
        if e == el:
            continue
        changed = order ^ (e > el)
        if changed:
            (M,Mi) = (m,mi) = (el, i-1)

        order = e>el
        m,mi = minI(m, mi, e, i)
        M,Mi = maxI(M, Mi, e, i)

        if M - m > d[0]:
            d = [M - m, [M,m],[Mi,mi]]

        el = e

    (dd, (M,m),(Mi,mi)) = d
    l,r = min(mi,Mi), max(mi,Mi)
    return d + [a[l:r+1]]

A = range(29)

import random

A = random.sample(A, len(A))

print(A)
print(maxseq(A))
