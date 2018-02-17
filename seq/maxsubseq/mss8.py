import random

def maxi(a,i,b,j):
    return (a,i) if a>b else (b,j)

def mini(a,i,b,j):
    return (a,i) if a<b else (b,j)

def maxseq(a):
    if len(a) <= 1:
        return 0

    d = 0

    m, M, mi, Mi, le = a[0], a[0], 0, 0, a[0]

    A = []

    t = 1

    for i,e in enumerate(a):
        if e == le:
            continue
        elif (e>le and t == 1) or (e<le and t == -1):
            m,mi = mini(m,mi,e,i)
            M,Mi = maxi(M,Mi,e,i)
        else:
            A += [(M-m,m,M,mi,Mi)]
            m,mi = mini(le,i-1,e,i)
            M,Mi = maxi(le,i-1,e,i)
            t = -t
        le = e

    A += [(M-m,m,M,mi,Mi)]

    Ad = list(map(lambda x:x[0], A))
    i = Ad.index(max(Ad))

    return A[i]

A = range(26)
A = random.sample(A, len(A))

print (A)
print (maxseq(A))            
