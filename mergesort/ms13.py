A = [1,2,3,10,22,-1,-2,-3,3,4,5,6,7,-1000,0.2]

def merge(a,b):
    i,j = 0,0

    c = []
    while i+j < len(a) + len(b):
        if i == len(a):
            c += [b[j]]
            j += 1
            continue

        if j == len(b):
            c += [a[i]]
            i += 1
            continue

        if a[i] < b[j]:
            c += [a[i]]
            i += 1
        else:
            c += [b[j]]
            j += 1


    # i on A, j on B
    # if f(a[i], b[j])
    #
    # stable construction:
    #   c += [e[x]]
    #   x += 1

    return c

def msort(a):
    p = int(len(a)/2)

    if p == 0:
        return a

    return merge(msort(a[:p]),msort(a[p:]))

print msort(A)
