# 05.11.2017
# start 16:02
# end   16:29 (w. long tests)


import numpy as np
import random
import math

np.set_printoptions(precision = 2, suppress = True)

def genDat(n,l):
    rotL = lambda x: x[1:] + [x[0]]
    rand = lambda y: map(lambda n:random.choice([0,1]),[0]*y)

    x = map(rand, [l] * n)
    y = map(rotL, x)

    x = map(np.array, x)
    y = map(np.array, y)

    return zip(x,y)


dat = genDat(10,5)

def logsigmoid(z):
    return 1.0/(1 + math.exp(-z))

def dlogsigmoid(z):
    f = logsigmoid
    return f(z)* (1 - f(z))

class NN:
    def __init__(_, ll, lr = 0.05):
        _.ll = ll
        _.lr = lr

        _.fA  = np.vectorize(logsigmoid)
        _.dfA = np.vectorize(dlogsigmoid)
        _.w, _.b = _.genWB()

    def genWB(_):
        w = [np.random.randn(n,m) for (n,m) in zip(_.ll[:-1], _.ll[1:])]
        b = [np.random.randn(m) for (m) in _.ll[1:]]

        return w,b

    def ff(_,x):
        v  = [None]*len(_.ll)
        vf = [None]*len(_.ll)

        vf[0] = v[0] = x
        for i in range(len(_.w)):
            v[i+1]  = np.dot(np.transpose(_.w[i]), vf[i]) + _.b[i]
            vf[i+1] = _.fA(v[i+1])

        return v,vf

    def ffp(_,x):
        v = x
        for i in range(len(_.w)):
            v  =  _.fA(np.dot(np.transpose(_.w[i]), v) + _.b[i] )

        return v


    def fb(_,v,vf, y):
        g  = [None] * len(_.w)
        gw = [None] * len(_.w)

        g[-1 ] = (vf[-1] - y) * (_.dfA(v[-1]))
        for i in range(len(_.w) -2, -1, -1):
            g[i] = np.multiply(np.dot(_.w[i+1], g[i+1]), _.dfA(v[i+1]))

        for i in range(len(_.w) -1, -1, -1):
            gw[i] = np.transpose(np.outer(g[i], vf[i]))

        return gw, g

    def trainStep(_,x,y):
        v,vf   = _.ff(x)
        gw, gb = _.fb(v,vf,y)

        _.w = _.w - np.multiply(gw, _.lr)
        _.b = _.b - np.multiply(gb, _.lr)

        out = _.ffp(x)

        [e1,e2] = [_.err(vf[-1],y), _.err(out,y)]
        # aml have to prognose the idea (I HOPE)
        # from algo idea db

        return [e1,e2]

    def train(_, data):
        return [_.trainStep(x,y) for (x,y) in data]

    def test (_, data):
        for (x,y) in data:
            out = _.ffp(x)
            e   = _.err(out,y)
            print "x = {}, y = {}, out = {}, e = {}".format(x,y,out,e)

    def err(_, out,y ):
        return math.sqrt(sum((out - y) ** 2))


layers = [[5,5,5], [5,6,5,5], [5,6,4,5], [5,6,3,5], [5,6,4,3,5]]


dat = genDat(300000,5)


for ll in layers :
    print ""
    print "ll = {}".format(ll)
    bbnn = NN(ll)
    print "before train"
    bbnn.test(dat[:10])
    bbnn.train(dat)
    print "after  train"
    bbnn.test(dat[:10])

# todo: avg, max error
