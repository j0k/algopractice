# 18.01.2018 15:56
# em502
# after Facebook interview

def mss(seq):
    dist = 0

    if len(seq)<=1:
        return dist

    last_trend = 0
    trend = 0

    mi, ma = seq[0], seq[0]
    for (el, er) in zip(seq[:-1], seq[1:]):
        if el == er:
            pass
        elif el < er:
            trend = 1
        else:
            trend = -1

        if last_trend != 0 and last_trend != trend:
            mi = min(el, er)
            ma = max(el, er)
        else:
            mi = min(mi, er)
            ma = max(ma, er)

        dist = max(dist, ma - mi)
        last_trend = trend

    return dist


A = [10,20,30,40,50,40,30,40,50,60,80]

import random


A = random.sample(range(1,100),40)

print(A)
print(mss(A))
