# 11.07.2017 3:13

def merge(a,b):
    i = j = 0

    c = []
    while (i+j) < len(a) + len(b):
        if i == len(a):
            c += [b[j]]
            j += 1
        elif j == len(b):
            c += [a[i]]
            i += 1
        else:
            if a[i] < b[j]:
                c += [a[i]]
                i += 1
            else:
                c += [b[j]]
                j += 1

    return c

def msort(a):
    if len(a) <= 1:
        return a

    m = int(len(a)/2)

    return merge(msort(a[:m]), msort(a[m:]))

A = [-10,2,3,4,5,6,-23,4,-1234,0,0,0,0,10]
print msort(A)
