import random

def maxi(a,b,ai,bi):
    return (a,ai) if a>b else (b, bi)

def mini(a,b,ai,bi):
    return (a,ai) if a<b else (b, bi)

def maxseq(a):
    d = 0

    if len(a) <= 1:
        return d

    m, M, le, mi, Mi = a[0], a[0], a[0], 0, 0

    trend = 0
    for i, e in enumerate(a):
        if e == le:
            continue
        elif e > le:
            if trend >= 0:
                trend = 1
                m, mi = mini(m, e, mi, i)
                M, Mi = maxi(M, e, Mi, i)
            else:
                trend = 1
                m, mi = mini(le, e, i -1, i)
                M, Mi = maxi(le, e, i -1, i)
        else:
            if trend <= 0:
                trend = -1
                m, mi = mini(m, e, mi, i)
                M, Mi = maxi(M, e, Mi, i)
            else:
                trend = -1
                m, mi = mini(le, e, i -1, i)
                M, Mi = maxi(le, e, i -1, i)
        le = e
    d = M - m
    return d, mi, Mi

A = range(20)
A = random.sample(A, len(A))

print(A)
d,mi,Mi = maxseq(A)
l, r = min(mi,Mi), max(mi,Mi)
print(A[l:r+1],l,r)
print(d)
