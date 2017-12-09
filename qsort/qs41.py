# 09.12.2017 20:10 CardPay, Cyprus

def qs(a):
    if len(a)<=1:
        return a

    p  = int(len(a)/2)

    ep = a[p]
    lr = [[],[]]
    for i,ai in enumerate(a):
        if i != p:
            lr[not ai <= ep] += [ai]

    return qs(lr[0]) + [ep] + qs(lr[1])

import random

A = range(26)
A = random.sample(A, len(A))

print A
print qs(A)
