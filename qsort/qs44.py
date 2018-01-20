def qs(a):
    if len(a) <= 1:
        return a

    lr = [[],[]]
    p = int(len(a)/2)

    for i,e in enumerate(a):
        if i == p:
            continue
        else:
            lr[not e <= a[p]] += [e]

    return qs(lr[0]) + [a[p]] + qs(lr[1])

A = range(28)

import random
A = random.sample(A, len(A))

print(A)
print(qs(A))


# 20.01.2018 23:53 em502 total 3 min
