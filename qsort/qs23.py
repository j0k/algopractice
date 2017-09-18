# 08.09.2017
# 12:19

def qsort(a):
    p = len(a)/2

    if p == 0:
        return a

    l,r = [],[]

    for i in range(len(a)):
        if i == p:
            continue

        if a[i] <= a[p]:
            l += [a[i]]
        else:
            r += [a[i]]

    return qsort(l) + [a[p]] + qsort(r)

import random
def randperm(a):
    l = len(a)
    for i in range(l):
        p = random.randint(0,l-1)
        a[i], a[p] = a[p], a[i]

    return a

A = randperm(range(20))

print A
print qsort(A)
# AML syntax example
# if a[i] <= a[p]:
#     l += [a[i]]
# else:
#     r += [a[i]]
#
# i != p:
#     m = choose{l,r}[! (a[i] <= a[p])]
#     m += [a[i]]

#
# if we write    m = choose{l,r}[! (a[i] <= a[p])]
# it's equal     m = ref choose{l,r}[! (a[i] <= a[p])]
# we can write   m = new choose{l,r}[! (a[i] <= a[p])]
# means
