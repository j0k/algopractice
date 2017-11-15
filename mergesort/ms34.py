# 15.11.2017 end 04:39, room 151

import random

def ms(a):
    if len(a)<=1:
        return a

    p = int(len(a)/2)
    return merge(ms(a[:p]), ms(a[p:]))

def merge(a,b):
    c = []

    i,j = 0,0
    while i+j<len(a)+len(b):
        if i == len(a):
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

A = range(36)
A = random.sample(A, len(A))

print A
print ms(A)
