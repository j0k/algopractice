# 25.06.2017
# exp

def msort(a):
    l = len(a)
    if l<=1:
        return a

    print "msort"
    p = int(len(a)/2)

    return merge(qsort(a[:p]), qsort(a[p:]))

def merge(a,b):
    li= i = j = 0

    c = []
    if (len(a) + len(b)) == 0:
        return c
    print "merge"

    while (i + j) < len(a)+len(b):
        if i == len(a):
            c += [b[j]]
            j += 1
        elif j == len(b):
            c += [a[i]]
            i += 1
        else:
            if a[i]<=b[j]:
                c += [a[i]]
                i += 1
            else:
                c += [b[j]]
                j += 1
    return c

def qsort(a):
    l = len(a)
    if l<=1:
        return a
    print 'qsort'

    p = int(len(a)/2)
    L,R = [],[]

    for i in range(len(a)):
        e = a[i]
        if i == p:
            continue
        if e <= a[p]:
            L += [e]
        else:
            R += [e]
    return msort(L) + [a[p]] + msort(R)

A = [10,2,3,4,4,-3,4,-10,200,201,0,0,4,5]
print msort (A)
