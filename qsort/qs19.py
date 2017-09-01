def qsort(a):
    if len(a) <= 1:
        return a

    l, m, r = [],[],[]
    plm, prm  = len(a)/3, len(a)*2/3

    if plm == prm:
        pass

    elm, erm = a[plm], a[prm]
    elm, erm = min(elm,erm), max(elm,erm)


    if plm == prm:
        del a[plm]
    else:
        inds = [plm,prm]

        del a[inds[1]]
        del a[inds[0]]

    for i in range(len(a)):
        e = a[i]
        if e <= elm:
            l += [e]
        elif e > elm and e <= erm:
            m += [e]
        else:
            r += [e]

    return qsort(l) + [elm] + qsort(m) + [erm] + qsort(r) if plm != prm else qsort(l) + [elm] + qsort(r)

import random

def randperm(a):
    for i in range(len(a)):
        c = a[i]
        p = random.randint(0,len(a)-1)
        a[i] = a[p]
        a[p] = c

    return a

A = randperm(range(20))

print A
print qsort(A)

###.
###. how to do that in AML
###.

###. qsort(a, k=2):
###.   ret a if len(a)<=1
###.   uni = unique
###.   pa = uni  ((i/k) * len(a)) in i:1 .. k-1
###.   (ep,pa) = uni(sort( a[i] {i}/@ pa ).order_on(pa) ).by([0])
###.
###.   na = [] * #ep
###.   for i in range(len(a)):
###.     continue if i in pa
###.     na[x] += [a[i]] where x = i {
###.                                    where a[i] < ep[x]: where x = 0
###.                                    where ep[x] <= a[i]: where x = -1 // x = #ep
###.                                    where ep[x] <= a[i] < ep[x+1]: where x = all
###.                                  }
###.   merge a,b = *a[0],b[0],*a[1],b[1], ...  // here we need a very powerful quesser
###.   ret merge(qsort /@ na,ep)
###.
