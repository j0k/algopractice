# 24.11.2017 11:15 cyprus cardpay

def me(a, b):
    i,j=0,0
    c
    while i+j<len(a)+len(b):
        if i==len(a):
            c += [b[j]]
            j += 1
        elif j == len(b):
            c += [a[i]]
            i += 1
        elif a[i] <= b[j]:
            c += [a[i]]
            i += 1
        else:
            c += [b[j]]
            j += 1
    return c

def ms(a):
    p = int(len(a)/2)

    if p <1:
        return a

    return me(ms(a[:p]), ms(a[p:]))


import random

A = range(25)
A = random.sample(A,len(A))

print A
print ms(A)
