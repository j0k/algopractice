def qsort(a):
    if len(a) <= 1:
        return a

    l, m, r = [],[],[]
    plm, prm  = len(a)/3, len(a)*2/3

    if plm == prm:
        pass

    elm, erm = a[plm], a[prm]
    elm, erm = min(elm,erm), max(elm,erm)


    if plm == prm:
        del a[plm]
    else:
        inds = [plm,prm]
        inds.sort()
        del a[inds[1]]
        del a[inds[0]]

    for i in range(len(a)):
        e = a[i]
        if e <= elm:
            l += [e]
        elif e > elm and e <= erm:
            m += [e]
        else:
            r += [e]

    return qsort(l) + [elm] + qsort(m) + [erm] + qsort(r) if plm != prm else qsort(l) + [elm] + qsort(r)

import random

def randperm(a):
    for i in range(len(a)):
        c = a[i]
        p = random.randint(0,len(a)-1)
        a[i] = a[p]
        a[p] = c

    return a

A = randperm(range(20))

print A
print qsort(A)
