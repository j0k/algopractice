import random

def mini(a,i,b,j):
    return (a,i) if a<=b else (b,j)

def maxi(a,i,b,j):
    return (a,i) if a>=b else (b,j)

def maxseq(a):
    if len(a) <= 1:
        return 0

    m,M,mi,Mi = a[0], a[0], 0, 0
    el = a[0]

    order = True
    d = [0, [M,m], [Mi,mi]]

    for (i,e) in enumerate(a):
        if e == el:
            continue

        if order ^ (e>el):
            m,mi = el,i-1
            M,Mi = el,i-1

        m,mi = mini(m,mi,e,i)
        M,Mi = maxi(M,Mi,e,i)

        order = e>el
        if M-m > d[0]:
            d = [M-m, [M,m], [Mi,mi]]
        el = e

    [dd, [M,m], [Mi,mi]] = d
    l,r = min(Mi,mi), max(Mi,mi)
    seq = a[l:r+1]

    return d + [seq]

A = range(28)

A = random.sample(A, len(A))

print(A)
print(maxseq(A))
