import random

def randpermute(a):
    for i in range(len(a)):
        pr = int(random.random() * len(a))
        c = a[pr]
        a[pr] = a[i]
        a[i] = c

    return a

def qsort(a):
    p = int(len(a)/2)

    if p == 0:
        return a

    m = a[p]
    del a[p]
    return qsort(filter(lambda x: x <= m, a)) + [m] + qsort(filter(lambda x: x > m, a))

A = randpermute(range(20) + [-100,100])

print qsort(A)

# return qsort(filter(lambda x: x <= m, a)) + [m] + qsort(filter(lambda x: x > m, a))
#
# here it will be useful to show compilator that it can be optimized into one flow
