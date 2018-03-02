def mini(a,i,b,j):
    return (a,i) if (a<b) else (b,j)

def maxi(a,i,b,j):
    return (a,i) if (a>b) else (b,j)

def maxseq(a):
    if len(a)<=1:
        return 0

    m,M,mi,Mi,el = a[0],a[0],0,0,a[0]

    d = 0
    seq = (m,M,mi,Mi,d)
    t = 1
    for i,e in enumerate(a):
        if e == el:
            continue
        elif (t == 1 and e>el) or (t == -1 and e<el):
            m,mi = mini(m,mi,e,i)
            M,Mi = maxi(M,Mi,e,i)
        else:
            m,mi = mini(el,i-1,e,i)
            M,Mi = maxi(el,i-1,e,i)
            t = -t

        if (M-m > d):
            d = M-m
            seq = (m,M,mi,Mi,d)

        el = e

    (m,M,mi,Mi,d) = seq
    l,r = min(mi,Mi), max(mi,Mi)

    return (a[l:r+1],seq)

import random

A = range(24)
A = random.sample(A, len(A))

print (A)
print( maxseq(A))
