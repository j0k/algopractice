# start at 02:20

# 18.01.2018 lima em502
def qs(a):
    if len(a) <= 1:
        return a

    p = int(len(a)/2)
    ap = a[p]
    lr = [[], []]

    for i,e in enumerate(a):
        if i == p:
            continue

        lr[not e<ap] += [e]

    return qs(lr[0]) + [ap] + qs(lr[1])

import random

A = range(27)
A = random.sample(A, len(A))

print(A)
print(qs(A))
