# 08.10.2017 11:54
# Sasha
# metro Primorskaya

def qs(a):
    if len(a) <= 1:
        return a

    p = int(len(a)/2)
    ep = a[p]

    l,r = [],[]
    for i,e in enumerate(a):
        if i == p:
            continue

        if e < ep:
            l += [e]
        else:
            r += [e]

    return qs(l) + [ep] + qs(r)

import random

A = range(30)
A = random.sample(A,len(A))

print A
print qs(A)
