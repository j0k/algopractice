import random
def qsort(a):
    p = int(len(a)/2)

    if p == 0:
        return a

    l,r = [],[]
    ep = a[p]

    for i in range(len(a)):
        if i == p:
            continue

        if a[i] < ep:
            l += [a[i]]

        else:
            r += [a[i]]

    return qsort(l) + [ep] + qsort(r)

def rp(a):
    for i in range(len(a)):
        p = random.randint(0,len(a)-1)
        a[i], a[p] = a[p], a[i]

    return a

A = rp(range(20))

print A
print qsort(A)
