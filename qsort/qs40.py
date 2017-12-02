def qs(a):
    if len(a)<1:
        return a

    p = int(len(a)/2)

    ap = a[p]

    lr = [[],[]]
    for i,e in enumerate(a):
        if not i == p:
            lr[not e <= ap] += [e]
            
    return qs(lr[0]) + [ap] + qs(lr[1])

import random

A = range(25)
A = random.sample(A, len(A))

print A
print qs(A)
