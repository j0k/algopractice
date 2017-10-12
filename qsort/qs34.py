import random

def qsort(a):
    p = int(len(a)/2)

    if p == 0:
        return a

    l,r = [],[]

    for i,e in enumerate(a):
        if i == p:
            continue

        if e <= a[p]:
            l += [e]
        else:
            r += [e]

    return qsort(l) + [a[p]] + qsort(r)

A = range(30)
A = random.sample(A, len(A))

print A
print qsort(A)
