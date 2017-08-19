def qsort(a):
    if len(a) <= 1:
        return a

    p = int(len(a)/2)
    ep = a[p]

    L,R = [],[]
    for i in range(len(a)):
        if i == p:
            continue

        if a[i] <= ep:
            L += [a[i]]
        else:
            R += [a[i]]

    return qsort(L) + [ep] + qsort(R)

A = [1,2,3,4,-7,44,5,-4,0,0,0,0,0,-100]

print qsort(A)
