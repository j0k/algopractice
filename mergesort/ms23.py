# 13.09.2017
# start 12:53
# endL 13:04

import random
def randperm(a):
    for i in range(len(a)):
        p = random.randint(0,len(a)-1)
        a[i], a[p] = a[p], a[i]

    return a

def merge(a,b):
    i,j = 0,0

    c = []

    while i+j < len(a) + len(b):
        if len(a) == i:
            c += [b[j]]
            j += 1
        elif len(b) == j:
            c += [a[i]]
            i += 1
        elif a[i] <= b[j]:
            c += [a[i]]
            i += 1
        else:
            c += [b[j]]
            j += 1

    return c

def msort(a):
    p = int(len(a)/2)

    if p == 0:
        return a

    return merge(msort(a[:p]), msort(a[p:]))

A = randperm(range(20))

print A
print msort(A)
