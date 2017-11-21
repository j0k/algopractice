# date: 20.11.2017
# time: 21:14
# time: 21:45
# after seq task: 10:30

import random
import math
import numpy as np

def genDat(n,l):
    rotL = lambda x: x[1:] + [x[0]]
    rand = lambda y: map(lambda e:random.choice([0,1]), [0]*y)

    x = map(rand, [l] * n)
    y = map(rotL, x)

    x = map(np.array, x)
    y = map(np.array, y)

    return zip(x,y)

def logsigmoid(x):
    return 1.0 / (1 + math.exp(-x))

def dlogsigmoid(x):
    f = logsigmoid
    return f(x) * (1 - f(x))


class NN:
    def __init__(_,ll,lr=0.05):
        _.lr = lr
        _.ll = ll
        _.w, _.b = _.genWB()
        _.fA  = np.vectorize(logsigmoid)
        _.dfA = np.vectorize(dlogsigmoid)

    def genWB(_):
        w = [np.random.randn(n,m) for (n,m) in zip(_.ll[:-1], _.ll[1:])]
        b = [np.random.randn(m)   for     m in _.ll[1:]]

        return w,b

    def ff(_,x):
        v  = [None] * len(_.ll)
        vf = [None] * len(_.ll)

        v[0]  = x
        vf[0] = x

        for i in range(len(_.w)):
            v[i+1]  = np.dot(np.transpose(_.w[i]), vf[i]) + _.b[i]
            vf[i+1] = _.fA(v[i+1])

        return v,vf

    def ffp(_,x):
        v = x
        for i in range(len(_.w)):
            v = _.fA(np.dot(np.transpose(_.w[i]), v) + _.b[i])
        return v

    def fb(_,v,vf,y):
        g  = [None]*len(_.w)
        gw = [None]*len(_.w)

        g[-1] = (vf[-1] - y) * _.dfA(v[-1])
        for i in range(len(_.w)-2,-1,-1):
            g[i]  = np.multiply(np.dot(_.w[i+1], g[i+1]), _.dfA(v[i+1]))

        for i in range(len(_.w)-1,-1,-1):
            gw[i] = np.transpose(np.outer(g[i], vf[i]))

        return g,gw

    def trainStep(_,x,y):
        v,vf = _.ff(x)
        g,gw = _.fb(v,vf,y)

        # print _.w
        # print gw
        # print map(lambda x:np.multiply(x,_.lr), gw)
        # print zip(_.w, map(lambda x:np.multiply(x,_.lr), gw) )

        minus = lambda lr: lr[0]-lr[1]
        _.w  = map(minus, zip(_.w, map(lambda x:np.multiply(x,_.lr), gw) ) )
        _.b  = _.b  - np.multiply(g,  _.lr)

        out  = _.ffp(x)
        [e1,e2] = [_.err(vf[-1],y), _.err(out,y)]

        return [e1, e2]

    def err(_,out,y):
        return math.sqrt( sum( (out - y) ** 2 ) )

    def train(_, data):
        return [_.trainStep(x,y) for (x,y) in data]

    def test(_, data, n):
        maxe,i = 0,0
        maxout = None
        for (x,y) in data:
            out = _.ffp(x)
            e   = _.err(out,y)
            if maxe<e:
                maxe = max(maxe,e)
                maxout = [x,y,out]

            if i<n:
                print "x={},y={},out={},e={}".format(x,y,out,round(e))
                i += 1
        print "max e = {}, maxout = {}".format(maxe, maxout)


def genSeq101(n,p):
    s = sum(p)
    p = map(lambda x:int(100 * x/s), p)

    seq   = [-1, 0, +1]
    items = []
    for i,e in enumerate(seq):
        items += [seq[i]] * p[i]

    return map(lambda x:random.choice(items), [0]*n)

def bs(seq):
    if len(seq) >= 1:
        if seq[0] == 0:
            return [seq[0]] + bs(seq[1:])

        if len(seq) >= 2:
            if seq[0] == -seq[1]:
                return seq[:2] + bs(seq[2:])
            else:
                return [seq[0], -seq[0]] + bs(seq[1:])
        else:
            return [seq[0], -seq[0]]


    return seq


def genSeqData(n,l):
    genSeq = lambda l: genSeq101(l,[2,6,2])
    x1     = map(lambda x: genSeq(x),      [l]*n)
    x2     = map(lambda red: bs(red), x1)

    y = []
    for i in range(len(x1)):
        y += [[(x1[i] == x2[i]) * 1.0]]

    return zip(x1,y)

data = genSeqData(1000000,4)

layers = [[4,1], [4,4,1], [4,3,1], [4,3,2,1], [4,4,4,4,1], [4,8,7,6,1],[4,8,1],[4,16,1],[4,8,16,1],[4,8,12,16,1],[4,16,12,8,4,1]]

#data = genDat(20,3)

for ll in layers:
    print "ll = {}".format(ll)
    nn = NN(ll)
    nn.train(data)
    nn.test(data,15)
    print "[] second iter"
    nn.train(data)
    nn.test(data,15)

for ll in layers:
    print "ll = {}".format(ll)
    nn = NN(ll)
    nn.train(data)
    nn.test(data,15)
    print "[] second iter"
    nn.train(data)
    nn.test(data,15)
