# 22.06.2017

A = [1,3,10,-1,20,30,-10,2]

def qsort(a):
    l = len(a)
    p = int(l/2)

    if l<=1:
        return a

    e = a[p]

    L,R = [],[]
    for i in range(l):
        if i != p:
            ai = a[i]
            if ai <= e:
                L += [ai]
            else:
                R += [ai]

    return qsort(L)+[e]+qsort(R)

print qsort(A)
