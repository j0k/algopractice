def ms(a):
    if len(a)<=1:
        return a

    p = len(a)/2

    c = []
    i,j = 0,0

    l,r = ms(a[:p]),ms(a[p:])
    while i+j<len(l)+len(r):
        if i == len(l):
            c += [r[j]]
            j += 1
        elif j == len(r):
            c += [l[i]]
            i += 1
        elif l[i] <= r[j]:
            c += [l[i]]
            i += 1
        else:
            c += [r[j]]
            j += 1

    return c


import random

A = range(25)
A = random.sample(A,len(A))

print A
print ms(A)
