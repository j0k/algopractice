def bins(a, e, l=0, n=0):
    if len(a) == 0:
        return -1

    p = int(len(a)/2)

    ep = a[p]

    if ep == e:
        return (l+p,n)
    elif ep > e:
        return bins(a[:p], e, l, n+1)
    else:
        return bins(a[p+1:], e, l+p+1, n+1)

A = range(50)

import random

Es = random.sample(A, 5)

for e in Es:
    p = bins(A, e)
    print("{e} is on p={p}".format(e=e, p=p))
