def qsort(a):
    if len(a) <= 1:
        return a

    p = int(len(a)/2)

    l, r = [],[]
    ap = a[p]

    for i,e in enumerate(a):
        if i == p:
            continue

        if e<=ap:
            l += [e]
        else:
            r += [e]

    return qsort(l) + [ap] + qsort(r)

import random

A = range(20)
A = random.sample(A,len(A))

print A
print qsort(A)
