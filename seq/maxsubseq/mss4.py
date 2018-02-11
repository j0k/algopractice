import random

def mseq(a):
    d = 0

    if len(a)<=1:
        return d

    m, M, el = a[0], a[0], a[0]

    trend = 0

    for i,e in enumerate(a):
        if trend == 0:
            if e == el:
                continue
            elif e > el:
                trend = 1
                m = min(m, e)
                M = max(M, e)
            else:
                trend = -1
                m = min(m, e)
                M = max(M, e)
        elif trend == 1:
            if e == el:
                continue
            elif e > el:
                m = min(m, e)
                M = max(M, e)
            else:
                trend = -1
                m = min(el, e)
                M = max(el, e)
        elif trend == -1:
            if e == el:
                continue
            elif e < el:
                m = min(m, e)
                M = max(M, e)
            else:
                trend = 1
                m = min(el, e)
                M = max(el, e)
        el = e
        d2 = max(d, M - m)

        if d2 > d:
            d = d2
    return d

A = range(10)
A = random.sample(A, len(A))

print(A)
print(mseq(A))

# aml:
# extended fields

# m, m_i = max(a)
#
# max(a,b): each a,b has $_i
#     e = a if a<=b else b
#     return e, e_i

# e_, i_ = max(a, b) | e = max(a,b), e_i
