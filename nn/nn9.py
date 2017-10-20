# start 20.10.2017
# time start: 9h 23m
# time end: 9h 45m
# total time: 22m

import random
import math
import numpy as np

def genDat(n,l):
    vec3 = lambda x: map(lambda x: random.choice([0,1]), range(l))
    x = map(vec3, range(n))

    rotL = lambda x:x[1:] + [x[0]]
    y = map(rotL, x)

    x = map(conv2v,x)
    y = map(conv2v,y)

    return zip(x,y)

def conv2v(v):
    return np.array(v).reshape(len(v),1)

def sigmoid(x):
    return 1.0/(1 + math.exp(-x))

class NN:
    def __init__(self,ll,lr=0.05):
        self.ll = ll
        self.lr = lr
        self.w, self.b = self.genWB()

    def genWB(self):
        ll = self.ll

        w = [np.random.randn(nin,nout) for (nin, nout) in zip(ll[:-1], ll[1:])]
        b = [np.random.randn(nout,1)   for nout        in ll[1:]]

        return w,b

    def ff(self,x):
        v  = [None for l in self.ll]
        vf = [None for l in self.ll]

        v[0]  = x
        vf[0] = x
        f = np.vectorize(sigmoid)

        for i in range(len(self.w)):
            v[i+1]  = np.dot(np.transpose(self.w[i]),v[i]) + self.b[i]
            vf[i+1] = f(v[i+1])

        return v,vf

    def fb(self,v,vf,y):
        f  = np.vectorize(sigmoid)
        df = lambda x: (1 - f(x)) * f(x)

        g  = [None for wi in self.w]
        gw = [None for wi in self.w]
        gb = [None for wi in self.w]

        g[-1] = (vf[-1] - y)*df(v[-1])

        for i in range(len(self.w) -2,-1,-1):
            g[i] = np.multiply( np.dot(self.w[i+1], g[i+1]), df(v[i+1]))

        for i in range(len(self.w) -1,-1,-1):
            gw[i] = np.transpose(np.outer(g[i], v[i]))

        return gw, g

    def trainStep(self,x,y):
        v,vf  = self.ff(x)
        gw,gb = self.fb(v,vf,y)

        mult = lambda x: np.multiply(x,self.lr)
        gw = map(mult, gw)
        gb = map(mult, gb)

        div = lambda x: x[0] - x[1]

        self.w = map(div, zip(self.w, gw))
        self.b = map(div, zip(self.b, gb))

        v2,vf2  = self.ff(x)

        [e1,e2] = self.err(vf[-1], y), self.err(vf2[-1], y)
        return [e1,e2]

    def err(self,yout, y):
        return math.sqrt(sum((yout - y)**2))

    def todo(self,data,f):
        return [f(x,y) for (x,y) in data]

    def train(self,data):
        return self.todo(data,self.trainStep)



dat = genDat(10000,3)

layers = [[3,4,3], [3,6,3]]

for ll in layers:
    nn = NN(ll)
    print "ll = {}".format(ll)
    nn.train(dat)
    print nn.train(dat[:10])
