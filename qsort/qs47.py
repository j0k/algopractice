def qs(a):
    if len(a)<=1:
        return a
    cp = int(len(a)/2)
    ce = a[cp]

    l, r = [], []
    for i,e in enumerate(a):
        if i == cp:
            continue
        else:
            if e < ce:
                l += [e]
            else:
                r += [e]

    return qs(l) + [ce] + qs(r)


import numpy as np

A = list(map(lambda x: int(x * 20), np.random.random_sample(30)))

print(A)
print(qs(A))
