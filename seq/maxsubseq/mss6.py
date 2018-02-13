def mini(a,ai,b,bi):
    return (a,ai) if a<=b else (b,bi)


def maxi(a,ai,b,bi):
    return (a,ai) if a>b else (b,bi)

def maxseq(a):
    d = 0

    if len(a)<=1:
        return a

    m, M, le = a[0], a[0], a[0]

    mi,Mi = 0,0
    trend = 1

    seq  = []
    seqi = []
    for i,e in enumerate(a):
        if e == le:
            continue
        elif (trend == 1 and e > le) or (trend == -1 and e < le):
            m,mi = mini(m,mi,e,i)
            M,Mi = maxi(M,Mi,e,i)
        else:
            seqi += [(mi,Mi)]
            seq  += [(m,M)]
            m,mi = mini(le,i-1,e,i)
            M,Mi = maxi(le,i-1,e,i)
            trend = -trend
        le = e

    seqi += [(mi,Mi)]
    seq  += [(m,M)]

    D = list(map(lambda x: x[1] - x[0], seq ))

    MM = max(D)
    ii = D.index(MM)
    l,r = seqi[ii]
    l,r = min(l,r), max(l,r)
    return MM,seq[ii], seqi[ii],a[l:r+1]

import random

A = range(25)
A = random.sample(A, len(A))

print (A)
print (maxseq(A))
