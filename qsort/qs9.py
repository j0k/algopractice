def qsort(a):
    if len(a)<=1:
        return a

    p = int(len(a)/2)

    ep = a[p]
    L,R = [],[]

    for i in range(len(a)):
        if i != p:
            if a[i]<=ep:
                L += [a[i]]
            else:
                R += [a[i]]

    return qsort(L) + [ep] + qsort(R)

A = [1,2,3,-2,3,4,-5,-10,20,30,-123,0,0,3,0,-20]

print qsort(A)
