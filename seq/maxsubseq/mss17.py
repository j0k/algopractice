def mini(a,i,b,j):
    return (a,i) if a<b else (b,j)

def maxi(a,i,b,j):
    return (a,i) if a>b else (b,j)

def maxseq(a):
    if len(a) <= 1:
        return 0

    d = 0
    m,M,mi,Mi,el = a[0], a[0], 0, 0, a[0]

    t = True
    A = []
    for i,e in enumerate(a):
        if e == el:
            continue
        if (t and e > el) or (not t and e < el):
            m, mi = mini(e,i,m,mi)
            M, Mi = maxi(e,i,m,mi)
        else:
            m, mi = mini(e,i,el,i-1)
            M, Mi = maxi(e,i,el,i-1)
            t = not t
        if M-m>d:
            l,r = min(mi,Mi), max(mi,Mi)
            d = M - m
            A = [d, M, m, mi, Mi, a[l:r+1]]

        el = e

    return A

A = range(27)
import random

A = random.sample(A, len(A))

print(A)
print(maxseq(A))
