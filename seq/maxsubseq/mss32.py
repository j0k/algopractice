import numpy as np

def maxi(a, ai, b, bi):
    return (a,ai) if a>=b else (b,bi)

def mini(a, ai, b, bi):
    return (a,ai) if a<=b else (b,bi)

def maxseq(a):
    if len(a)<=1:
        return 0

    m,mi = a[0],0
    M,Mi = a[0],0
    lv = a[0]

    o, ol = True, True
    d = [0]
    for i,v in enumerate(a):
        if v == lv:
            continue

        o = v > lv
        changed = (o ^ ol)

        if changed:
            m,mi = mini(v,i,lv,i-1)
            M,Mi = maxi(v,i,lv,i-1)
        else:
            m,mi = mini(v,i,m,mi)
            M,Mi = maxi(v,i,M,Mi)

        if M-m > d[0]:
            l,r = min(mi,Mi), max(mi,Mi)
            d = [M-m, (m,mi,M,Mi), a[l:r+1]]
        ol = o
        lv = v
    return d


A = list(map(lambda x: int(x * 10), np.random.random_sample(10)))
print(A)
print(maxseq(A))
