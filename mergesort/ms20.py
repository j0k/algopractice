def msort(a):
    p = int(len(a)/2)
    if p == 0:
        return a

    a1 = msort(a[:p])
    a2 = msort(a[p:])

    i,j = 0,0
    c = []

    while i + j < len(a1) + len(a2):
        if i == len(a1):
            c += [a2[j]]
            j += 1
        elif j == len(a2):
            c += [a1[i]]
            i += 1
        elif a1[i] <= a2[j]:
            c += [a1[i]]
            i += 1
        else:
            c += [a2[j]]
            j += 1

    return c

import random
def randperm(a):
    for i in range(len(a)):
        p = random.randint(0,len(a)-1)
        a[i], a[p] = a[p], a[i]
    return a

A = randperm(range(25))
print A
print msort(A)
