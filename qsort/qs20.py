def qsort(a):
    p = int(len(a)/2)

    if (p == 0):
        return a

    lr =[[],[]]
    for i in range(len(a)):
        if i == p:
            continue

        lr[a[i] > a[p]] += [a[i]]

    return qsort(lr[0]) + [a[p]] + qsort(lr[1])

import random
def rp(a):
    for i in range(len(a)):
        p = random.randint(0,len(a)-1)
        c = a[i]
        a[i] = a[p]
        a[p] = c
    return a

A = rp(range(20))
print A
print qsort(A)
