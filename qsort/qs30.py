def qsort(a):
    if len(a)<=1:
        return a

    p = int(len(a)/2)

    l,r = [],[]
    for i,e in enumerate(a):
        if i == p:
            continue

        if e < a[p]:
            l += [e]
        else:
            r += [e]

    return qsort(l) + [a[p]] + qsort(r)

import random

A = random.sample(range(20),20)

print A
print qsort(A)
