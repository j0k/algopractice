import random

def genSeq(n, p=None):
    l = ldef = [-1,0,1]

    if p != None:
        s = sum(p)
        p2 = map(lambda x:int(x/s *100), p)
        l = []
        for i,e in enumerate(p2):
            l += [ldef[i]] * e

    seq = map(lambda x:random.choice(l), [0] * n)
    return seq

def balanceSeq(seq):
    items = []
    ds = 0
    dl = 0
    i  = 0
    while i<len(seq):
        e      = seq[i]
        items += [e]
        ds    += e
        dl    += 1

        if e == 0:
            ds = 0
            dl = 0
        elif i+1<len(seq):
            en  = seq[i+1]
            dsn = ds + en
            dln = dl + 1
            if abs(dsn) >= 1:
                items += [-e]
        elif i+1 == len(seq):
            if abs(ds) >= 1:
                items += [-e]                

        i+=1
    return items, sum(items)



seq = genSeq(10,[0.4,0.8,0.1])
bseq = balanceSeq(seq)

print seq
print bseq
