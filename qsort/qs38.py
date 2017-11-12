def qs(a):
    if len(a)<=1:
        return a

    c = int(len(a)/2)
    ec = a[c]

    lr = [[], []]
    for i,e in enumerate(a):
        if i == c:
            continue

        lr [not e<= ec] += [e]

    lr = map(qs, lr)
    return lr[0] + [ec] + lr[1]

import random
A = range(25)
A = random.sample(A, len(A))

print A
print qs(A)
