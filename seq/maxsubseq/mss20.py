# 29.03.2018 13:44 metro (go to ingria)

import random

def desc_seq(a,i,I):
    m, M = a[i], a[I]
    l,r  = min(i,I), max(i,I)
    seq  = a[l:r+1]
    d    = M - m

    h = {
        'seq'     : seq,
        'd'       : d,
        'min-max' : [m,M],
        'seq'     : seq,
        'inds'    : [i,I]
    }

    return h

def mini(a,i,b,j):
    return (a,i) if a<=b else (b,j)

def maxi(a,i,b,j):
    return (a,i) if a>=b else (b,j)

def maxseq(a):
    if len(a)<=1:
        return 0

    m, M, mi, Mi, el = a[0], a[0], 0, 0, a[0]
    d, t = 0, True

    A = [mi,Mi]
    for i,e in enumerate(a):
        if e == el:
            continue

        elif (e>el and t) or (e<el and not t):
            m,mi = mini(m,mi,e,i)
            M,Mi = maxi(M,Mi,e,i)
        else:
            m,mi = mini(el,i-1,e,i)
            M,Mi = maxi(el,i-1,e,i)
            t    = not t
        el = e

        if M-m > d:
            A = [mi,Mi]
            d = M-m

    return desc_seq(a, A[0], A[1])

A = range(30)

A = random.sample(A, len(A))

print(A)
print(maxseq(A))

# aml:
# + stmt with properties
#
