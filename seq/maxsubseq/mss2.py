def mss(seq):
    trend = 0
    d = 0
    for (i,e) in enumerate(seq):
        if i == 0:
            le = e
            mi = e
            ma = e


        if le == e:
            pass
        elif le < e:
            if trend >= 0:
                mi = min(mi,e)
                ma = max(ma,e)
            else:
                mi = min(le,e)
                ma = max(le,e)
            trend = 1
        else:
            if trend <= 0:
                mi = min(mi,e)
                ma = max(ma,e)
            else:
                mi = min(le,e)
                ma = max(le,e)
            trend = -1
        d = max(d, ma - mi)
        le = e

    return d

A = [1,2,3,4,4,5,6,7,3,-1,-3,12]
print(A)
print(mss(A))
