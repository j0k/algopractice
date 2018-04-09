# 09.04.2018 151 22:30 start

def minI(a,i,b,j):
    return (a,i) if a < b else (b,j)

def maxI(a,i,b,j):
    return (a,i) if a > b else (b,j)

import random

def mss(a):
    if len(a) <= 1:
        return 0

    m,mi, M,Mi = a[0],0, a[0],0

    el = a[0]
    order = True
    d = [0]

    for (i,e) in enumerate(a):
        if e == el:
            continue

        changed = order ^ (e>el)
        if changed:
            M,Mi = m,mi = el,i-1
        m,mi = minI(m,mi,e,i)
        M,Mi = maxI(M,Mi,e,i)

        if M - m > d[0]:
            d = [M-m, [M,m], [Mi,mi]]

        order = e>el
        el = e # in AML : at the end of the block el = e  /:end

    li,ri = d[-1]
    li,ri = min(li,ri), max(li,ri)
    return d + [a[li:ri+1]]

A = range(28)
A = random.sample(A, len(A))

print(A)
print(mss(A))
