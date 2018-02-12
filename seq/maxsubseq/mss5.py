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
    bm, bM, bmi, bMi = a[0], a[0], 0, 0

    trend = 1

    def sb():
        bm,bmi = mini(bm, m, bmi, mi)
        bM,bMi = maxi(bM, M, bMi, Mi)

    for i, e in enumerate(a):
        if e == le:
            continue
        elif (e > le and trend > 0) or (e < le and trend < 0):
            # trend not change
            m, mi = mini(m, e, mi, i)
            M, Mi = maxi(M, e, Mi, i)

        else:
            # here we need to save the best result
            trend = -trend
            if M-m > bM - bm:
                bm,bmi = m, mi
                bM,bMi = M, Mi

            m, mi = mini(le, e, i - 1, i)
            M, Mi = maxi(le, e, i - 1, i)

        le = e

    if M-m > bM - bm:
        bm,bmi = m, mi
        bM,bMi = M, Mi

    d = bM - bm
    return d, bmi, bMi

A = range(20)
A = random.sample(A, len(A))

print(A)
d,mi,Mi = maxseq(A)
l, r = min(mi,Mi), max(mi,Mi)
print(A[l:r+1],l,r)
print(d)
