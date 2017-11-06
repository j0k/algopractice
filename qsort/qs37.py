def qs(a):
    if len(a)<=1:
        return a

    lr = [[],[]]
    p   = int(len(a)/2)
    c  = a[p]

    for i in range(len(a)):
        if i == p:
            continue

        lr[not (a[i]<= c)] += [a[i]]

    l,r = map(qs, lr)
    return l + [c] + r

import random

A = range(25)
A = random.sample(A, len(A))

print A
print qs(A)
