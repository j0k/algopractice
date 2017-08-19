# 14.07.2017

def centersort(a):
    if len(a) <= 1:
        return a

    l,r = [],[]

    i,j = 0,0

    m = len(a)
    p = int(m/2)
    for i in range(p):
        if a[i] > a[m-1 - i]:
            c = a[m-1 - i]
            a[m-1 - i] = a[i]
            a[i] = c

    l,r = centersort(a[:p]), centersort(a[p:])
    b = l + r
    for i in range(p):
        if b[i] > b[m-1 - i]:
            c = b[m-1 - i]
            b[m-1 - i] = b[i]
            b[i] = c


    return b

A = [1,2,3,4,-1,2,3,4,-1,-2,-10,-20,-123,-11,100,1000]

print centersort(A)
