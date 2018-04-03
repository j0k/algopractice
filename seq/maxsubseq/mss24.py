# 02/04/2017

def maxi(a, i, b, j):
    return (a,i) if a>b else (b,j)

def mini(a, i, b, j):
    return (a,i) if a<b else (b,j)

def maxseq(a):
    if len(a) <= 1:
        return 0

    m,M, mi,Mi = a[0], a[0], 0, 0
    el = a[0]
    order = True

    for i,e in enumerate(a):
        if e == el:
            continue

        changed = (e > el) ^ order
        if changed:
            m, mi = mini(el, i-1, e, i)
            M, Mi = maxi(el, i-1, e, i)
        else:
            m, mi = mini(m, mi, e, i)
            M, Mi = maxi(M, Mi, e, i)

        if d < M-m:
            d = M-m
        el = e
        order = e > el

    return d

A = range(30)

import random
A = random.sample(A, len(A))

print(A)
print(maxseq(A))
