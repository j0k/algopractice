def qsort(a):
    if len(a)<= 1:
        return a

    p = int(len(a)/2)

    e = a[p]
    l,r = [],[]

    for i in range(len(a)):
        ai = a[i]
        if i == p:
            continue

        if a[i]<=e:
            l += [ai]
        else:
            r += [ai]

    return qsort(l) + [e] + qsort(r)

import random
def rp(a):
    return random.sample(a,len(a))

A = rp (range(20))
print A
print qsort(A)
