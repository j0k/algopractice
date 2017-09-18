def merge(a,b):
    i,j,c = 0,0,[]

    while i + j < len(a) + len(b):
        if i == len(a):
            c += [b[j]]
            j += 1
            continue

        if j == len(b):
            c += [a[i]]
            i += 1
            continue

        if a[i] <= b[j]:
            c += [a[i]]
            i += 1
        else:
            c += [b[j]]
            j += 1

    return c

def msort(a):
    p = int(len(a)/2)
    return merge(msort(a[:p]),msort(a[p:])) if p > 0 else a

import random
def rp(a):
    for i in range(len(a)):
        p = random.randint(0,len(a)-1)
        a[i], a[p] = a[p], a[i]

    return a

A = rp(range(15))
print A
print msort(A)
