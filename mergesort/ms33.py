# date: 14.11.2017
# 12:11. total 4-6 min

import random

def ms(a):
    if len(a)<=1:
        return a

    p = int(len(a)/2)

    l,r = map(ms, [a[:p] , a[p:]])

    i,j = 0,0
    c = []
    while i+j<len(l) + len(r):
        if i == len(l):
            c += [r[j]]
            j += 1
        elif j == len(r):
            c += [l[i]]
            i += 1
        elif l[i] <= r[j]:
            c += [l[i]]
            i += 1
        else:
            c += [r[j]]
            j += 1

    return c

A = range(29)
A = random.sample(A, len(A))

print A
print ms(A)
