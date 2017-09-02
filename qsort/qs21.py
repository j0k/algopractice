def qsort(a):
    p = int(len(a)/2)

    if p == 0:
        return a

    ep = a[p]
    l,r = [],[]
    for i in range(len(a)):
        e = a[i]

        if i == p:
            continue

        if e < ep:
            l += [e]
        else:
            r += [e]

    return qsort(l) + [ep] + qsort(r)



import random
def rp(a):
    for i in range(len(a)):
        p = random.randint(0, len(a) - 1)
        a[i], a[p] = a[p], a[i]

    return a

A = rp(range(15))
print A
print qsort(A)
