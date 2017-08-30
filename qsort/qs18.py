def qsort(a):
    filt = lambda a, when: filter(lambda x: when(x), a)
    p = int(len(a)/2)

    if p == 0:
        return a

    e = a[p]
    left  = lambda x: x <= e
    right = lambda x: x >  e

    del a[p]

    # print " AP ", e
    # print " qsL: " , filter(left,a)
    # print " qsR: " , filter(right,a)
    return qsort(filter(left,a)) + [e] + qsort(filter(right,a))

A = [1,5,2,3,10,10,-100,101,-1,-2,0,0,0]

print A
print qsort(A)

# AML:
# left, right = (<=, >) e
# a[^i]
