A = [3,2,3,4,5,2,3,4,5,3,0,0,10,100,-100,10,122,102,-2]

def qsort(a):
    p = len(a)/2

    if p == 0:
        return a

    ep = a[p]

    l, r = [], []

    for i in range(len(a)):
        e = a[i]

        if i == p:
            continue

        if e <= ep:
            l += [e]
        else:
            r += [e]

    return qsort(l) + [ep] + qsort(r)

print qsort(A)
# C-fast code compatible paradigm

# mistakes:
#if e <= ep: was if ep <= e:
#    l += [e] was l += [ep]
#else: was else
#    r += [e] was r += [ep]
