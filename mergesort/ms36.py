# 11:42 03/12/2017 flat502

def merge(a,b):
    i,j = 0,0
    c = []
    for k in range(len(a) + len(b)):
        ai = k - i
        bj = k - j

        if len(a) == ai:
            c += [b[bj]]
            i += 1
        elif len(b) == bj:
            c += [a[ai]]
            j += 1
        elif a[ai] <= b[bj]:
            c += [a[ai]]
            j += 1
        else:
            c += [b[bj]]
            i += 1

    return c


import random

A = range(27)
A = random.sample(A, len(A))

print A

def ms(a):
    p = int(len(a)/2)

    if p == 0:
        return a

    return merge(ms(a[:p]), ms(a[p:]))

print ms(A)
