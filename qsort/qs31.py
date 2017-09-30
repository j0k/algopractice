import random

def qs(a):
    if len(a) <= 1:
        return a

    p = random.randint(0,len(a)-1)
    ap = a[p]

    l,r = [],[]
    for i,e in enumerate(a):
        if i == p:
            continue

        if e<=ap:
            l += [e]
        else:
            r += [e]

    return qs(l) + [ap] + qs(r)

A = range(25)
A = random.sample(A,len(A))

print A
print qs(A)
