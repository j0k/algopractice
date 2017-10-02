# 02.10.2017
# 14:38

import random

def merge(a,b):
    i,j = 0,0
    c = []
    while i+j < len(a) + len(b):
        if i == len(a):
            c += [b[j]]
            j += 1
        elif j == len(b):
            c += [a[i]]
            i += 1
        elif a[i] < b[j]:
            c += [a[i]]
            i += 1
        else:
            c += [b[j]]
            j += 1

    return c

def ms(a):
    if len(a)<=1:
        return a

    p = random.randint(0,len(a)-1)

    return merge(ms(a[:p]), ms(a[p:]))

A = range(20)
A = random.sample(A,len(A))

print A
print ms(A)
