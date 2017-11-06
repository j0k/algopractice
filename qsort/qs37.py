# 07.11.2017
# Spb, 151, end: 12:43

def qs(a):
    if len(a)<=1:
        return a

    lr = l,r = [[],[]]
    p   = int(len(a)/2)
    c  = a[p]

    for i,ai in enumerate(a):
        if i == p:
            continue

        lr[not (ai <= c)] += [ai]

    l,r = map(qs, lr)
    return l + [c] + r

import random

A = range(25)
A = random.sample(A, len(A))

print A
print qs(A)

# TODO: aml
# multiple verison
# a1,a2,a3,a4 = [], [], [], []
# ediv = len(#a[..]) - 1
