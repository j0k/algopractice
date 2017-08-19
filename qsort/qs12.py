# 16.07.2017

def qsort(a):
    if len(a)<=1:
        return a

    p = int(len(a)/2)
    e = a[p]

    LR = [[],[]]
    for i in range(len(a)):
        if i == p:
            continue

        LR[ 1 - (a[i] <= a[p]) ] += [a[i]]

    return qsort(LR[0]) + [e] + qsort(LR[1])

A = [1,2,3,-1,2,3,0,0,-1,100,10,123,-1.2,-1000]

print qsort(A)
