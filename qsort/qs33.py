import random

def qs(a):
    if len(a)<=1:
        return a

    l,r = [],[]
    p = int(len(a)/2)

    for i,e in enumerate(a):
        if i == p:
            continue

        if e <= a[p]:
            l += [e]
        else:
            r += [e]

    return qs(l) + [a[p]] + qs(r)

A = range(20)
A = random.sample(A,len(A))

print A
print qs(A)
