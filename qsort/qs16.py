from random import random

def qsort(a):
    if len(a)<=1:
        return a

    p = int(random() * len(a))
    e = a[p]

    c = [[],[]]
    for i in range(len(a)):
        if i == p:
            continue

        c[(a[i] > e)] += [a[i]]

    return qsort(c[0]) + [e] + qsort(c[1])

def randpermute(a):
    for i in range(len(a)):
        p = int(random() * len(a))

        c = a[p]
        a[p] = a[i]
        a[i] = c

    return a

A = randpermute(range(20))
print A
print qsort(A)
