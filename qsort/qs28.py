def qsort(a):
    if len(a) <= 1:
        return a

    p   = int(len(a)/2)

    ep  = a[p]
    l,r = [],[]

    for i in range(len(a)):
        ai = a[i]
        if i == p:
            continue

        if ai <= ep:
            l += [ai]
        else:
            r += [ai]

    return qsort(l) + [ep] + qsort(r)

import random

A = range(20)

A = random.sample(A,len(A))
print A
print qsort(A)
