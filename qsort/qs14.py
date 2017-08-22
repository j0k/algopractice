def qsort(a):
    p = int(len(a)/2)

    if p == 0:
        return a

    c = [[],[]]
    for i in range(len(a)):
        if p == i:
            continue

        c[(a[i] >= a[p])] += [a[i]]

    return qsort(c[0]) + [a[p]] + qsort(c[1])

A = [1,2,3,2,3,4,-10,-100,-12,14,35,13,26,39,0.001]

print(qsort(A))

#     return qsort(c[0]) + [a[p]] + qsort(c[1])
# qsort @@ (c[0], ^@ [a[p]], c[1])
# ^@ - don't apply

#f @^@ x = x
#   ^@ x = x
#f  ^@:f,g x = x
#h  ^@:f,g x = h(x)
#f  ^@:^f x  = f(x)
#h  ^@:^f x  = x

#function combining paradigm
