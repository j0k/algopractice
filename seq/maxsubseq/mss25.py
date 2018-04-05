import random

def mini(a,i,b,j):
    return (a,i) if a<b else (b,j)

def maxi(a,i,b,j):
    return (a,i) if a>b else (b,j)

def minmax(a,i,m,mi,M,Mi):
    return mini(a,i,m,mi) + maxi(a,i,M,Mi)

def maxseq(a):
    if len(a)<=1:
        return 0

    m, M, el = a[0], a[0], a[0]
    mi = Mi = 0
    d = 0

    order = True
    changed = False

    for (i,e) in enumerate(a):
        if el == e:
            continue

        changed = (e > el) ^ order
        #print(changed)
        if changed:
            m, mi, M, mi = minmax(e,i,el,i-1,el,i-1)

        else:
            m, mi, M, mi = minmax(e,i,m,mi,M,Mi)

        order = e>el
        el = e

        #print(i, M-m,M,m)
        if d<M-m:
            d = M-m
            print(i, M-m,M,m)

    return d

A = range(23)

A = random.sample(A, len(A))

print(A)
print(maxseq(A))

# AML loop: current, last =last:1, last_last=last:2, last:3, ... , last:n
# order = (e > el)
# changed = order:last ^ order
# principle 
