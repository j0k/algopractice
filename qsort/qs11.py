# 13.07.2017

def qsort(a):
    if len(a) <= 1:
        return a

    p = int(len(a)/2)
    ep,ap,pa = a[p],a[:p],a[p+1:]

    L,R = [],[]
    for e in ap + pa:
        if e <= ep:
            L += [e]
        else:
            R += [e]


    return qsort(L) + [ep] + qsort(R)

A = [1,2,3,4,5,-1,-2,-3,0,0,0,10,123,-123]

print qsort(A)
