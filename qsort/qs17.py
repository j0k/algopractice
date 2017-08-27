from random import random

def rande(a):
    return int(random() * len(a))

def change(a,i,p):
    c = a[i]
    a[i] = a[p]
    a[p] = c

    return a

def qsort(a):
    if len(a) <= 1:
        return a

    p = rande(a)
    e = a[p]

    c = [[],[]]
    for i in range(len(a)):
        if i == p:
            continue

        c[a[i] > e] += [a[i]]

    return qsort(c[0]) + [e] + qsort(c[1])


def randperm(a):
    for i in range(len(a)):
        change(a, rande(a), i)
        
    return a


A = randperm(range(15))
print(A)
print(qsort(A))
