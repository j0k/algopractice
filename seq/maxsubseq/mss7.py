import random

def maxi(a,i,b,j):
    return (a,i) if a>b else (b,j)

def mini(a,i,b,j):
    return (a,i) if a<b else (b,j)


def maxseq(a):
    if len(a) <= 1:
        return 0

    d = 0
    m,M,le, mi, Mi = a[0], a[0], a[0], 0, 0


    t = 1
    A = []
    for i,e in enumerate(a):
        if e == le:
            continue
        if (e>le and t==1) or (e<le and t==-1):
            M, Mi = maxi(M,Mi,e,i)
            m, mi = mini(m,mi,e,i)
        else:
            A += [(M-m, m,mi,M,Mi)]
            t = -t
            M, Mi = maxi(le, i-1, e, i)
            m, mi = mini(le, i-1, e, i)
        le = e

    A += [(M-m, m, mi, M, Mi)]

    Ad = list(map(lambda x:x[0], A))
    Ad_max = max(Ad)

    Ad_max_i = Ad.index(Ad_max)
    return A[Ad_max_i]

A = list(range(26))

A = random.sample(A, len(A))

print(A)
print(maxseq(A))
