# 22.06.2017

A = [1,40,23,67,68,-67,-69,8,8,8,9,-1,-100,3]

def msort(a):
    l = len(a)
    p = l/2

    if l <= 1:
        return a

    maL = msort(a[:p])
    maR = msort(a[p:])

    return merge(maL,maR)

def merge(a,b):
    if len(a) == 0 or len(b) == 0:
        return a + b
    i = 0
    j = 0

    c = []

    while i<len(a) or j < len(b):
        if i==len(a):
            c += [ b[j] ]
            j += 1
            continue

        if j==len(b):
            c += [ a[i] ]
            i += 1
            continue

        if a[i] <= b[j]:
            c += [ a[i] ]
            i += 1
        else:
            c += [ b[j] ]
            j += 1

    return c

print msort(A)


# a(2:20] - elements from (2 to 20]
# it's not usefull but in general it's very cool
