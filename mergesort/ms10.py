def fmerge(f,a,b):
    c = []

    i = j = 0

    while (i+j) < (len(a) + len(b)):
        if i == len(a):
            c += [b[j]]
            j += 1
        elif j == len(b):
            c += [a[i]]
            i += 1
        else:
            # c += [a[i]] if f(a[i],b[j]) else b[j]
            if f(a[i],b[j]):
                c += [a[i]]
                i += 1
            else:
                c += [b[j]]
                j += 1

    return c

def merge(a,b):
    return fmerge(lambda x,y: x<=y, a, b)

def msort(a):
    p = int(len(a)/2)

    if p == 0:
        return a

    return merge(msort(a[:p]),msort(a[p:]))

A = [1,2,3,4,1,2,3,3,0,0,0,0,0,-100,100,0]

print msort(A)
