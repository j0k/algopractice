import random


def maxi(a,i,b,j):
    return (a,i) if a>b else (b,j)
def mini(a,i,b,j):
    return (a,i) if a<b else (b,j)

def subseq(a,p1,p2):
    return a[min(p1,p2):max(p1,p2)+1]

def maxseq(a):
    if len(a)<=1:
        return 0

    d = 0
    m,M,el = a[0],a[0],a[0]

    mi,Mi = 0,0
    t = True
    R = []
    for i,e in enumerate(a):
        if el == e:
            continue
        if (t and e>el) or ((not t) and e<el):
            m,mi = mini(e,i,m,mi)
            M,Mi = maxi(e,i,M,Mi)
        else:
            m,mi = mini(el, i-1, e, i)
            M,Mi = maxi(el, i-1, e, i)
            t = not t

        if (M-m > d):
            d = M -m
            R = [d, M, m, Mi, mi, subseq(a,mi,Mi)]
        el = e

    return R

seq = range(25)
seq = random.sample(seq, len(seq))

print(seq)
print(maxseq(seq))
