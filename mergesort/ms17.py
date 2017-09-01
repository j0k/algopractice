def merge(a,b):
    inds = [0,0]

    argv = [a,b]
    c = []
    def change(ind,i):
        c.append(argv[ind][i])
        inds[ind] += 1

    while sum(inds) < len(a) + len(b):
        i,j = inds
        if i == len(a):
            change(1,j)
        elif j == len(b):
            change(0,i)
        elif a[i] <= b[j]:
            change(0,i)
        else:
            change(1,j)

    return c


def msort(a):
    p = int(len(a)/2)
    if p == 0:
        return a

    return merge(msort(a[:p]), msort(a[p:]))

import random

def randperm(a):
    for i in range(len(a)):
        p = random.randint(0,len(a)-1)
        c = a[i]
        a[i] = a[p]
        a[p] = c

    return a


A = randperm(range(20))
print A
print msort(A)
