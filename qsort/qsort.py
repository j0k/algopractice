# 17.06.2017

import random

A = [1,4,7,2,3,5,7,9,1,1,20,30,40,606,7,3,4,5,20,30,40,50,5,4,8,88,88,888,10]

def qsort(a):
    l = len(a)
    print l

    p = int(random.random() * l)
    if l>1:
        elem = a[p]
        del a[p]

        left  = qsort(filter(lambda x : x <= elem, a))
        right = qsort(filter(lambda x : x >  elem, a))

        # really we have to make one filter operation
        return left + [elem] + right
    else:
        return a;


sortA = qsort(A)

print sortA
