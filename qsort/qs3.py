# 20.06.2017

import random

A = [1,10,2,4,5,6,6,6,1,1,1,-2,-10,0,200,23]

def qsort(a):
    if len(a)<= 1:
        return a

    l = int(len(a) * random.random())
    p = a[l]

    L,R = [],[]
    # error for i in range(l): 
    for i in range(len(a)):
        if i == l: continue
        # error if i != l: continue
        e = a[i]
        L.append(e) if e <= p else R.append(e)

    return qsort(L) + [p] + qsort(R)
    # error     return qsort(L) , [p] , qsort(R)


print qsort(A)
