# 18.06.2017

import random

A = [1,2,4,7,8,9,0,5,3,5,6,8,4,3]

def qsort(a):
    l = len(a)

    if l <= 1:
        return a

    pi = int(random.random() * l)

    left = []
    right = []

    p = a[pi]
    for (i,item) in enumerate(a):
        if i == pi:
            continue;
        if item <= p:
            left.append(item)
        else:
            right.append(item)

    return qsort(left) + [p] + qsort(right)

print qsort(A)
