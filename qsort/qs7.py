def qsort(a):
    l = len(a)
    if l<=1:
        return a

    p = int(l/2)

    aa = [[],[]]

    for i in range(l):
        if i == p:
            continue
        e = a[i]
        aa[(e <= a[p])] += [e]

    return qsort(aa[1]) + [ a[p] ] + qsort(aa[0])

A = [1,2,3,4,2,3,4,-2,-3,100,-100,0,0,0]

print qsort(A)
