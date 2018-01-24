# 16.10.2017
# start: 15:21
# end:   16:49
# total time: 1h 28m
# end that exp: 17:14
# total time with exp: 1h 53m

import random
import numpy as np
import math

np.set_printoptions(precision=2,suppress=True)
#np.set_printoptions(suppress=True)

def genDat(n,l):
    rotL  = lambda x : x[1:] + [x[0]]
    rotR  = lambda x : [x[-1]] + x[:-1]

    rand  = lambda x : random.choice([0.0,1.0])
    randL = lambda x : map(rand, range(l))

    x = map(randL, range(n))
    y = map(lambda x : rotL(x) + rotR(x) , x)

    return zip(x,y)

def sigmoid(z):
    return 1.0/(1.0 + math.exp(-z))

class NN:
    def __init__(self, ll, LR = 0.05):
        self.ll        = ll
        self.LR        = LR
        self.w, self.b = self.genWB()

    def genWB(self):
        ll = self.ll
        w = [np.random.randn(inN,outN) for (inN,outN) in zip(ll[:-1],ll[1:])]
        b = [np.random.randn(outN,1)   for outN       in ll[1:]]

        return w,b

    def ff(self,x):
        w = self.w
        b = self.b
        f = np.vectorize(sigmoid)

        v     = [None for i in self.ll]
        v[0]  = x

        vf    = [None for i in self.ll]
        vf[0] = x

        for i in range(len(w)):
            v[i+1]  = np.dot(np.transpose(w[i]),v[i]) + b[i]
            vf[i+1] = f(v[i+1])

        return v,vf

    def fb(self,v,vf,x,y):
        w  = self.w
        b  = self.b

        f  = np.vectorize(sigmoid)
        df = lambda z: (1 - f(z))*f(z)

        grad  = [None for x in w]
        gradw = [None for x in w]
        gradb = [None for x in w]

        grad[-1] = (vf[-1] - y) * df(v[-1]) # why v[-1] not vf[-1]

        #print len(grad), len(v)
        for i in range(len(grad) -2, -1,-1):
            grad[i] = np.multiply(np.dot(w[i+1], grad[i+1]) , df(v[i+1]))


        for i in range(len(grad)-1,-1,-1):
            #pass
            gradw[i] = np.outer( grad[i], v[i])
            #print "gradw[{}]={}".format(i,gradw[i])
            #print "grad[{}]", grad[i]

        gradw = map(np.transpose,gradw)
        gradb = grad

        return gradw, gradb

    def trainStep(self,x,y):
        v,vf         = self.ff(x)
        gradw, gradb = self.fb(v,vf,x,y)

        #print gradw
        gradwmult = map(lambda x:np.multiply(x, self.LR), gradw)

        self.w = map(lambda x:x[0] - x[1], zip(self.w,gradwmult))
        self.b = self.b - np.multiply(gradb, self.LR)

        return self.err(vf[-1],y)

    def err(self, out, y):
        return math.sqrt(sum((out - y) ** 2))

    def todo(self,dat,f):
        res = []
        for x,y in dat:
            x    = np.array(x).reshape(len(x),1)
            y    = np.array(y).reshape(len(y),1)
            res += [f(x,y)]

        return res

    def train(self,dat):
        errs = self.todo(dat, self.trainStep)
        step = int(len(errs)/10)
        errs_parts = [errs[x:x+step] for x in xrange(0, len(errs), step)]
        return map(np.mean,errs_parts)

    def test(self,dat):
        self.todo(dat, self.testXY)

    def testXY(self,x,y):
        v,vf = self.ff(x)
        err  = self.err(vf[-1],y)
        print "x = {}, y = {}, out = {}, err = {}".format(nF(x),nF(y),nF(vf[-1]),err)

def nF(v):
    return np.transpose(v)[0]


dat = genDat(10000,3)
print dat[:10]

layers = [[3,3,6],[3,4,6],[3,2,6],[3,3,5,6],[3,6]]

for ll in layers:
    print "ll = {}".format(ll)
    nn = NN(ll)
    for x,y in dat:
        x    = np.array(x).reshape(len(x),1)
        y    = np.array(y).reshape(len(y),1)
        v,vf = nn.ff(x)
        nn.fb(v,vf,x,y)
        nn.trainStep(x,y)
    print "avg errors = {}".format(nn.train(dat))

    nn.test(dat[:10])
