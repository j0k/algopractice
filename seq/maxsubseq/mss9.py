# flat 151
# 19.02.2018 14:30 schpagating
# 19.02.2018 14:39 end

import random

def maxi(a,i,b,j):
    return (a,i) if a>=b else (b,j)

def mini(a,i,b,j):
    return (a,i) if a<=b else (b,j)


def maxseq(a):
    if len(a) <= 1:
        return a

    m,M,mi,Mi,le = a[0], a[0], 0, 0, a[0]

    A = []
    t = 1
    for i,e in enumerate(a):
        if e != le:

            if (t == 1 and e>le) or (t == -1 and e < le):
                m,mi = mini(m,mi,e,i)
                M,Mi = maxi(M,Mi,e,i)
            else:
                m,mi = mini(le,i-1,e,i)
                M,Mi = maxi(le,i-1,e,i)
                t = -t

                A += [(M-m,m,mi,M,Mi)]
        le = e

    A += [(M-m,m,mi,M,Mi)]
    Ad = list(map(lambda x:x[0], A))

    i = Ad.index(max(Ad))

    (d,m,mi,M,Mi) = A[i]
    l,r = min(mi,Mi), max(mi,Mi)
    return (d, mi, Mi, m, M, a[l:r+1])

A = list(range(27))
A = random.sample(A, len(A))

print(A)
print(maxseq(A))
