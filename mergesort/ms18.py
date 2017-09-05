# start time: don't write
# end time: 05.09.2017 11:24
# worked since first time

import random

def merge(a,b):
    inds = [0,0]

    A = [a,b]
    c = []
    def change(a,ind):
        i = inds[ind]
        c.append(a[i])
        inds[ind] += 1

    while sum(inds) < len(a) + len(b):
        i,j = inds
        if i == len(a):
            change(b,1)
        elif j == len(b):
            change(a,0)
        elif a[i] <= b[j]:
            change(a,0)
        else:
            change(b,1)
    return c


def msort(a):
    p = int(len(a)/2)

    if p == 0:
        return a
    return merge(msort(a[:p]), msort(a[p:]))

def rp(a):
    for i in range(len(a)):
        p = random.randint(0,len(a)-1)
        a[p], a[i] = a[i], a[p]

    return a

A = rp(range(25))
print A
print msort(A)
