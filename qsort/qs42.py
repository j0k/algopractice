def qs(a):
    if len(a)<=1:
        return a

    lr = [[],[]]
    p  = int(len(a)/2)
    ap = a[p]

    for i,e in enumerate(a):
        if i != p:
            lr[not e<=ap] += [e]

    return qs(lr[0]) + [ap] + qs(lr[1])

A = range(29)

import random

A = random.sample(A, len(A))

print A
print qs(A) 
