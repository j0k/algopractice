# 04092017 11:09 Limasol. CardPay office

def qsort(a):
    p = int(len(a)/2)

    if p == 0:
        return a

    e = a[p]
    del a[p]
    return qsort(filter(lambda x:x<=e,a)) + [e] + qsort(filter(lambda x:x>e,a))

import random
def rp(a):
    for i in range(len(a)):
        p = random.randint(0,len(a)-1)
        a[i],a[p] = a[p],a[i]
    return a

A = rp(range(15))
print A
print qsort(A)

# 04092017 11:16 end

# AML filtering:
#
# 
# return qs(<= e & .i!=p), (.i == p), qs(>e &.i !=p)  a
