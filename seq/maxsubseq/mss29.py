# 23:41 - 23:47 12.04.2018 room151

import random

def mini(a,i,b,j):
    return (a,i) if a<=b else (b,j)

def maxi(a,i,b,j):
    return (a,i) if a>=b else (b,j)

def maxseq(a):
    if len(a)<=1:
        return 0

    m,M,mi,Mi = a[0], a[0], 0, 0

    order = True
    el    = a[0]
    d     = [0]

    for (i,e) in enumerate(a):
        if e == el:
            continue

        if order ^ (e > el):
            m,mi = el,i-1
            M,Mi = el,i-1

        m,mi = mini(m,mi,e,i)
        M,Mi = maxi(M,Mi,e,i)

        if M-m>d[0]:
            l,r = min(mi,Mi), max(mi,Mi)
            d = [M-m,[M,m], [Mi,mi], a[l:r+1]]

        order = e>el
        el = e
    return d

A = range(28)
A = random.sample(A, len(A))

print(A)
print(maxseq(A))
