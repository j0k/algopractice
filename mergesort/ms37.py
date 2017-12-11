def ms(a):
    if len(a)<=1:
        return a

    p = int(len(a)/2)

    l = ms(a[:p])
    r = ms(a[p:])

    c = []

    i,j= 0,0

    # in aml:
    # close expression AML principle
    # idea i to l, j to r
    # i*: c += [l[i]], i++
    # if j == len(r): i*
    # elif i == len(l): j*
    # elif l[i] < r[j]: i*
    # else j*

    while i+j<len(l)+len(r):
        if j == len(r):
            c += [l[i]]
            i += 1
        elif i == len(l):
            c += [r[j]]
            j += 1
        elif l[i] <= r[j]:
            c += [l[i]]
            i += 1
        else:
            c += [r[j]]
            j += 1

    return c

import random

A = range(31)
A = random.sample(A, len(A))

print A
print ms(A)
