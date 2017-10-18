# 18.10.2017
# start: 19:08
# end: 19:49
# total time: 0h 41m

import random
import math
import numpy as np

np.set_printoptions(precision = 2, suppress = True)

def genDat(n,l):
    rotL = lambda x: x[1:] + [x[0]]

    randv = lambda x : map(lambda x2: random.choice([0,1]), range(l))

    x = map(randv, range(n))
    y = map(rotL, x)

    return zip(x,y)



def sigmoid(z):
    return 1.0/(1 + math.exp(-z))

class NN:
    def __init__(self, ll, LR = 0.05):
        self.ll = ll
        self.LR = LR
        self.w, self.b = self.genWB()

    def genWB(self):
        ll = self.ll
        w = [np.random.randn(nin, nout) for (nin, nout) in zip(ll[:-1],ll[1:])]
        b = [np.random.randn(nout, 1)   for nout        in ll[1:]]
        return w,b

    def ff(self,x):
        f     = np.vectorize(sigmoid)

        v     = [None for l in self.ll]
        vf    = [None for l in self.ll]

        v[0]  = x
        vf[0] = x

        for i in range(len(self.w)):
            v[i+1]  = np.dot( np.transpose(self.w[i]), v[i]) + self.b[i]
            vf[i+1] = f(v[i+1])

        return v, vf

    def fb(self,v,vf,y):
        f     = np.vectorize(sigmoid)
        df    = lambda z: (1 - f(z))*f(z)

        grad  = [None for tmp in range(len(self.w))]
        gradw = [None for tmp in range(len(self.w))]
        gradb = [None for tmp in range(len(self.w))]

        grad[-1] = (vf[-1] - y) * df(v[-1])


        for i in range(len(self.w)-2,-1,-1):
            grad[i] = np.multiply ( np.dot(self.w[i+1], grad[i+1]), df(v[i+1]))
            #print "g",grad[i]

        for i in range(len(self.w)-1,-1,-1):
            gradw[i] = np.transpose( np.outer(grad[i],v[i] ) )

        gradb = grad

        return gradw, gradb

    def trainStep(self,x,y):
        v, vf = self.ff(x)
        gw,gb = self.fb(v,vf,y)

        gw = map(lambda x: np.multiply(x,self.LR), gw)
        delta = lambda x,y : map(lambda z:z[0] - z[1], zip(x,y))

        self.w = delta(self.w, gw)
        self.b = delta(self.b, gb)

        v2,vf2 = self.ff(x)

        e1 = self.err(vf[-1] ,y)
        e2 = self.err(vf2[-1],y)

        return [e1,e2]


    def err(self, yN, y):
        return math.sqrt(sum((yN - y) ** 2))

    def train(self, data):
        cost = []
        tcost = []
        cnt = 0
        maxcnt = int(len(data)/10)

        for (x,y) in data:
            e1,e2 = self.trainStep(x,y)
            cnt += 1
            tcost += [e1]

            if maxcnt == 0 or cnt % maxcnt == 0:
                cost += [sum(tcost)/len(tcost)]
                tcost = []

        return cost

    def test(self,data):
        for (x,y) in data:
            v,vf = self.ff (x)
            e    = self.err(vf[-1],y)



            print "x = {}, y = {}, out = {}, e = {}".format(normF(x), normF(y), normF(vf[-1]), e)

def normF(v):
    return v.reshape(1,len(v))[0]

def toNPA(data):
    dat = []
    for (x,y) in data:
        x = np.array(x).reshape(len(x),1)
        y = np.array(y).reshape(len(y),1)
        dat += [(x,y)]

    return dat

dat = genDat(10000,4)
dat = toNPA(dat)

layers = [[4,4,4], [4,5,4], [4,3,4], [4,5,4,4]]

for ll in layers:
    for lr in [0.01,0.05,0.1,0.2,0.3]:

        print "ll = {}, lr = {}".format(ll, lr)
        nn = NN(ll,lr)
        for (x,y) in dat:
            v,vf = nn.ff(x)
            nn.fb(v,vf,y)
            nn.trainStep(x,y)

        print "errs = {}".format(nn.train(dat))
        nn.test(dat[:10])
