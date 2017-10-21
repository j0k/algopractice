def qs(a):
    p = int(len(a)/2)
    if p == 0:
        return a

    l, r = [],[]
    e    = a[p]

    for i,ai in enumerate(a):
        if i == p:
            continue

        if ai <= e :
            l += [ai]
        else:
            r += [ai]

    return qs(l) + [e] + qs(r)


import random
A = range(25)
A = random.sample(A,len(A))

print A
print qs(A)
