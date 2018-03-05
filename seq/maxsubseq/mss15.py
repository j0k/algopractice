import random

def maxseq(a):
    if len(a)<=1:
        return 0

    m, M, mi, Mi, el = a[0], a[0], 0, 0, a[0]

    t = True
    d = 0
    mm, MM = m, M
    for i,e in enumerate(a):
        if e == el:
            continue
        if (t and e>el) or (not t and e<el):
            m, M = min(m,e), max(M,e)
        else:
            m, M = min(el,e), max(el,e)
            t = not t

        if (d < M-m):
            d, MM, mm  = M-m, M, m
            print (d,M,m,t, e,el)
        el = e

    return d, MM, mm

A = range(26)
A = random.sample(A, len(A))

print(A)
print(maxseq(A))
