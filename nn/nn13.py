import random
import numpy as np
import math

def genDat(n,l):
    rotL = lambda x: x[1:] + [x[0]]

    rand  = lambda a,n: map(lambda y: random.choice(a), range(n))
    randL = lambda x  : rand([0,1], x)

    x = map(randL, [3] * n)
    y = map(rotL, x)

    x = map(np.array, x)
    y = map(np.array, y)

    return zip(x,y)

def logsigmoid(z):
    return 1.0/(1.0 + math.exp(-z))

def dlogsigmoid(z):
    return (1.0 - logsigmoid(z))*logsigmoid(z)

def logsigmoid2(z):
    if (-z) > 60:
        return -1.0
    else:
        return 2.0/(1.0 + math.exp(-z)) - 1.0

def dlogsigmoid2(z):
    return 2.0*(1.0 - logsigmoid2(z))*logsigmoid2(z)


class NN:
    def __init__(_, ll, lr = 0.05):
        _.ll  = ll
        _.lr  = lr
        _.w, _.b = _.genWB()
        _.fA  = np.vectorize(logsigmoid2)
        _.dfA = np.vectorize(dlogsigmoid2)


    def genWB(_):
        w = [np.random.randn(nin, nout)/5 for (nin, nout) in zip(_.ll[:-1], _.ll[1:])]
        b = [np.random.randn(nout)/5      for nout        in _.ll[1:]]

        return w,b

    def ff(_,x):
        v  = [None for l in _.ll]
        vf = [None for l in _.ll]

        v [0] = x
        vf[0] = x
        for i in range(len(_.w)):
            v[i+1] = np.dot(np.transpose(_.w[i]), vf[i]) + _.b[i]
            vf[i+1] = _.fA(v[i+1])

        return v,vf

    def fb(_,v,vf,y):
        g  = [None for i in _.w]
        gw = [None for i in _.w]

        g[-1] = (vf[-1] - y) * _.dfA(v[-1])

        for i in range(len(_.w) - 2,-1,-1):
            g[i] = np.multiply(np.dot(_.w[i+1], g[i+1]), _.dfA(v[i+1]))

        for i in range(len(_.w) - 1,-1,-1):
            gw[i] = np.transpose(np.outer(g[i], vf[i]))

        return gw,g

    def trainStep(_,x,y):
        v,vf  = _.ff(x)
        gw,gb = _.fb(v,vf,y)

        _.w     = _.w - np.multiply(gw, _.lr)
        _.b     = _.b - np.multiply(gb, _.lr)
        v2,vf2  = _.ff(x)

        [e1,e2] = _.err(vf[-1],y), _.err(vf2[-1],y)
        return [e1, e2]

    def err(_,out,y):
        return math.sqrt(sum( (out - y)**2 ))

    def train(_, data):
        return [_.trainStep(x,y) for (x,y) in data]

    def test(_,data):
        for (x,y) in data:
            v,vf = _.ff(x)
            e = _.err(vf[-1], y)
            print "x = {}, y = {}, out = {}, e = {}".format(x,y,vf[-1],e)


dat = genDat(100000,3)
layers = [[3,4,3], [3,5,3], [3,4,2,4,3]]

for ll in layers:
    print "ll = {}".format(ll)
    nn = NN(ll)
    print "Before TRAIN"
    nn.test(dat[:7])
    print nn.train(dat[:5])
    nn.train(dat)
    print "AFTER TRAIN"
    nn.test(dat[:7])
    print nn.train(dat[:5])
