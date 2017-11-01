import random

def qs(a):
    if len(a) <= 1:
        return a

    p = int(len(a)/2)
    e = a[p]

    l,r = [],[]
    for i,ai in enumerate(a):
        if i == p:
            continue

        if ai < e:
            l += [ai]
        else:
            r += [ai]

    return qs(l) + [e] + qs(r)


A = range(25)
A = random.sample(A, len(A))

print A
print qs(A)
