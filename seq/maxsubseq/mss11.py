import random

def mini(a,i,b,j):
    return (a,i) if (a<=b) else (b,j)

def maxi(a,i,b,j):
    return (a,i) if (a>=b) else (b,j)


def maxseq(a):
    if len(a) <= 1:
        return 0

    m,M,le,mi,Mi = a[0],a[0],a[0],0,0
    A = []

    t = 1

    d   = 0
    seq = []
    for i,e in enumerate(a):


        if (e == le):
            continue
        elif (e>le and t>0) or (e<le and t<1):
            m,mi = mini(m,mi,e,i)
            M,Mi = maxi(M,Mi,e,i)
        else:
            m,mi = mini(le,i-1,e,i)
            M,Mi = maxi(le,i-1,e,i)

        if (d < M - m):
            seq = (m,M,mi,Mi,M-m)
            d = M - m

        le = e

    (m,M,mi,Mi,d) = seq
    li = min(mi,Mi)
    ri = max(mi,Mi)

    return (d,mi,Mi,a[li:ri+1])

A = range(19)

A = random.sample(A, len(A))

print(A)
print(maxseq(A))
