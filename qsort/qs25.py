import random

def randperm(a):
    for i in range(len(a)):
        p = random.randint(0,len(a)-1)
        a[i], a[p] = a[p], a[i]

    return a

def qsort(a):
    if len(a) <=1:
        return a
    p = random.randint(0, len(a) - 1)

    e = a[p]

    l,r = [],[]
    for i in range(len(a)):
        if i == p:
            continue

        ai = a[i]
        if ai <= e:
            l += [ai]
        else:
            r += [ai]

    return qsort(l) + [e] + qsort(r)

A = randperm(range(20))

print A
print qsort(A)
