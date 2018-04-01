import random

def maxi(a,i,b,j):
    return (a,i) if a>=b else (b,j)

def mini(a,i,b,j):
    return (a,i) if a<=b else (b,j)

def maxseq(a):
    if len(a) <= 1:
        return 0

    m, M, mi, Mi, el = a[0], a[0], 0, 0, a[0]
    d = 0
    order = True

    for i,e in enumerate(a):
        if e  == el:
            continue

        changed = (e > el)  ^ order
        if changed:
            m,mi = mini(el,i-1,e,i)
            M,Mi = maxi(el,i-1,e,i)
        else:
            m,mi = mini(m, mi, e, i)
            M,Mi = maxi(M, Mi, e, i)

        order = (e>el)

        el = e
        if M-m > d:
            d = M-m

    return d

A = range(27)
A = random.sample(A, len(A))

print(A)
print(maxseq(A))
