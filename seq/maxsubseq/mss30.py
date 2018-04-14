import random

def mini(a,i,b,j):
    return (a,i) if (a<b) else (b,j)

def maxi(a,i,b,j):
    return (a,i) if (a>b) else (b,j)

def maxseq(a):
    if len(a)<=1:
        return 0

    m, M, mi, Mi = a[0], a[0], 0, 0
    order = True
    changed = False
    el = a[0]

    d = [0, [M,m],[Mi,mi],[]]
    for (i,e) in enumerate(a):
        if e == el:
            continue

        changed = order ^ (e<el)
        # print(i, e, changed)
        if changed:
            M,Mi = m,mi = el,i-1

        m,mi = mini(m,mi,e,i)
        M,Mi = maxi(M,Mi,e,i)

        if M-m>d[0]:
            l,r = min(mi,Mi), max(mi,Mi)
            d   = [M-m, [M,m], [Mi, mi],a[l:r+1]]

        order = e<el
        el = e

    return d

for i in range(100):
    A = range(29)
    A = random.sample(A, len(A))
    d = maxseq(A)
    if len(d[-1]) > 2 and d[-1][0]> d[-1][1]:
        print(A)
        print(maxseq(A))
        break;
