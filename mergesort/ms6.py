# 01.07.2017

def merge(a):
    i = j = 0
    if (sum(map(len,a)) <= 1):
        return a[0] + a[1]

    c = []
    while (i + j < sum(map(len,a))):
        if i == len(a[0]):
            c += [a[1][j]]
            j += 1
        elif j == len(a[1]):
            c += [a[0][i]]
            i += 1
        else:
            if a[0][i] <= a[1][j]:
                c += [a[0][i]]
                i += 1
            else:
                c += [a[1][j]]
                j += 1
    return c

def msort (a):
    if len(a)<=1:
        return a

    p = int(len(a)/2)

    return merge([msort(a[:p]) , msort(a[p:])] )

A = [1,2,3,-3,4,5,10,100,-100,-1000,3,-4]

print msort(A)
