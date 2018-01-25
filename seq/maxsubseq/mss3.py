# 25.01.2018 23:24 em502

def mss(a):
    mi,ma = 0,0
    d = 0

    if len(a)<=1:
        return d

    le = a[0]
    mi,ma = le,le
    trend = 0
    for i,e in enumerate(a):
        if le == e:
            pass
        if le < e:
            if trend == 1:
                mi = min(mi, e)
                ma = max(ma, e)
            else:
                mi = min(le,e)
                ma = max(le,e)
            trend = 1
        if le > e:
            if trend == -1:
                mi = min(mi, e)
                ma = max(ma, e)
            else:
                mi = min(le,e)
                ma = max(le,e)
            trend = -1
        d = max(d, ma-mi)

    return d

A = list(range(27))
import random

A = random.sample(A, len(A))
print(A)
print(mss(A))
