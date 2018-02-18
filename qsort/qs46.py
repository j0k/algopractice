# 18.02.2018 23:42 sta
# 18.02.2018 23:45 end

import random

def qs(a):
    if len(a)<=1:
        return a

    p  = int(len(a)/2)
    ep = a[p]

    lr = [[],[]]
    for i,e in enumerate(a):
        if i != p:
            lr[not e<ep] += [e]

    return qs(lr[0]) + [ep] + qs(lr[1])

A = list(range(28))
A = random.sample(A, len(A))

print (A)
print( qs(A))
