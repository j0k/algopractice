# Airport Pulkovo
# 12.10.2017 03:14

import random

def qsort(a):
    p = int(len(a)/2)

    if p == 0:
        return a

    l,r = [],[]

    for i,e in enumerate(a):
        if i == p:
            continue

        if e <= a[p]:
            l += [e]
        else:
            r += [e]

    return qsort(l) + [a[p]] + qsort(r)

A = range(30)
A = random.sample(A, len(A))

print A
print qsort(A)

### how it will be in AML:
###
###
# a += [e], where a = l if e <= a[p] else r
# a += [e] /. a = l if e <= a[p] else r

# aml example
#p,l,r = (int) len(a)/2, [], []
#not p == 0

#for e in a:
#    not e.i == p
#    a += [e] /. a = l if e <= a[p] else r

#return $f(l) + [a[p]] + $f(r)

###
#p,l,r = len(a)/2, [], []
#e in a[^p]
#  a += [e]
#    /. a = {e<=a[p]: l, r}

# {e<=a[p]: l, r} += [e] for e in a[^p]

# the same
# not e.i == p
# continue if e.i == p
