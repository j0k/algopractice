A = [1,2,3,4,1,23,4,1,2,3,4,0,-100,100]

def merge(a,b):
    c = []
    i,j = 0,0

    while (i + j) < (len(a) + len(b)):
        if i == len(a):
            c += [b[j]]
            j += 1
        elif j == len(b):
            c += [a[i]]
            i += 1
        else:
            if a[i] <= b[j]:
                c += [a[i]]
                i += 1
            else:
                c += [b[j]]
                j += 1

    return c

def msort(a):
    if len(a)<= 1:
        return a

    cp = int(len(a)/2)

    if cp == 0:
        return a

    ecp = a[cp]

    l,r = [],[]
    for i in range(len(a)):
        e = a[i]
        if i < cp:
            l += [e]
        else:
            r += [e]
        #if e <= ecp:
        #    l += [e]
        #else:
        #   r += [e]

    #print "L",l
    #print "R",r

    return merge(msort(l),msort(r))


print msort(A)
