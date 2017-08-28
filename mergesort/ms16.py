def merge(a,b):
    if len(a) + len(b) <=1:
        return a+b

    ii,ij = 0, 1
    ind = [0,0]
    c = []

    def go(a,i_):
        i = ind[i_]
        c.append(a[i])
        ind[i_] += 1

    while ind[0] + ind[1] < len(a) + len(b):
        i,j = ind
        if i == len(a):
            go(b, ij)
        elif j == len(b):
            go(a, ii)
        elif a[i] < b[j]:
            go(a, ii)
        else:
            go(b, ij)

    return c

def msort(A):
    p = int(len(A)/2)

    if p == 0:
        return A

    return merge( msort(A[:p]), msort(A[p:]))

from random import random

def randperm(a):
    for i in range(len(a)):
        p = int(len(a) * random())

        c = a[i]
        a[i] = a[p]
        a[p] = c

    return a

A = range(15)
A = randperm(A)
print A
print msort(A)


print merge([-10,1,2,2,3], [0,4,5,6])

# while ind[0] + ind[1] < len(a) + len(b):
#     i,j = ind
#     if i == len(a):
#         go(b, ij)
#     elif j == len(b):
#         go(a, ii)
#     elif a[i] < b[j]:
#         go(a, ii)
#     else:
#         go(b, ij)

# :: - means alias
# while :: i,j = ind
#     i+j < len /@ a,b:
#
#     :: goa, gob = go(a,ii), go(b,ij)
#     if i == len(a): goa
#        j == len(b): gob
#        a[i] < b[j]: goa
#        else       : gob
