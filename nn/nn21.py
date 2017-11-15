# 15.11.2017
# start: 22:41
# end: 00:01
# total: 1h 20m, most of time i discuss different things
# <o>

import numpy as np
import random

def genData(n,l):
    rotL = lambda x: x[1:] + [x[0]]

    rand = lambda x: map(lambda y:random.choice([0,1]), [0]*x)
    x    = map(rand, [l]*n)
    y    = map(rotL, x)

    x    = map(np.array, x)
    y    = map(np.array, y)
    return zip(x,y)

import math
def logsigmoid(z):
    return 1.0/(1 + math.exp(-z))

def dlogsigmoid(z):
    f = logsigmoid
    return f(z)*(1 - f(z))

class NN:
    def __init__(_, ll, lr=0.05):
        _.ll = ll
        _.lr = lr
        _.w, _.b = _.genWB()
        _.fA  = np.vectorize( logsigmoid  )
        _.dfA = np.vectorize( dlogsigmoid )

    def genWB(_):
        w = [np.random.randn(n,m) for (n,m) in zip(_.ll[:-1], _.ll[1:])]
        b = [np.random.randn(m)   for m     in _.ll[1:]]

        return w,b

    def ff(_,x):
        v  = [None] * len(_.ll)
        vf = [None] * len(_.ll)

        v[0] = vf[0] = x
        for i in range(len(_.w)):
            v[i+1]  = np.dot(np.transpose(_.w[i]), vf[i]) + _.b[i]
            vf[i+1] = _.fA(v[i+1])

        return v,vf

    def ff_pure(_,x):
        v  = x
        for i in range(len(_.w)):
            v = _.fA(np.dot(np.transpose(_.w[i]), v) + _.b[i])

        return v

    def fb(_, v,vf,y):
        g  = [None] * len(_.w)
        gw = [None] * len(_.w)

        g[-1] = (vf[-1] - y) * _.dfA(v[-1])

        for i in range(len(_.w)-2,-1,-1):
            g[i] = np.multiply(np.dot(_.w[i+1], g[i+1]), _.dfA(v[i+1]))

        for i in range(len(_.w)-1,-1,-1):
            gw[i] = np.transpose(np.outer(g[i], vf[i]))

        return g,gw

    def trainStep(_,x,y):
        v,vf  = _.ff(x)
        g,gw = _.fb(v,vf,y)

        _.w = _.w - np.multiply(gw, _.lr)
        _.b = _.b - np.multiply(g, _.lr)

        out = _.ff_pure(x)

        [e1,e2] = [_.err(vf[-1],y), _.err(out,y)]
        return [e1,e2]

    def err(_,out,y):
        return math.sqrt(sum((out - y) ** 2))

    def train(_,data):
        return [_.trainStep(x,y) for (x,y) in data]

    def test(_,data):
        for (x,y) in data:
            out = _.ff_pure(x)
            e   = _.err(out,y)
            print "x = {}, y = {}, out = {}, e = {}".format(x,y,out,e)


layers = [[3,3,3],[3,2,3], [3,4,5,2,3]]

data = genData(100000,3)

for ll in layers:
    print "ll = {}".format(ll)
    nn = NN(ll)
    nn.train(data)
    nn.test(data[:5])
