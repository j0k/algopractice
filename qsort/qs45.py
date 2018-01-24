# 24.01.2018 23:54 em502

def qs(a):
    if len(a)<=1:
        return a

    p = int(len(a)/2)

    ap = a[p]

    lr = [[],[]]
    for i,e in enumerate(a):
        if i != p:
            lr[not e <= ap] += [e]

    return qs(lr[0]) + [ap] + qs(lr[1])


A = range(27)

import random

A = random.sample(A, len(A))
print (A)
print (qs(A))
