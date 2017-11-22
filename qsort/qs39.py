# 22.11.2017 - end: 11:35, Old Hospital, Lima, Cyprus

import random

def qs(a):
    if len(a)<=1:
        return a

    p = len(a)/2
    lr = [[],[]]

    for i,e in enumerate(a):
        if not i == p:
            lr[not e <= a[p]] += [e]

    lr = map(qs, lr)
    return lr[0] + [a[p]] + lr[1]

A = range(25)
A = random.sample(A, len(A))

print A
print qs(A)
