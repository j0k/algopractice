# 17.10.2017
# start 14:14
# end   15:23
# total 1h 9m

import random
import numpy as np
import math

np.set_printoptions(precision=2,suppress =True)

def genDat(n,l):
    rotL = lambda x: x[1:] + [x[0]]

    rand = lambda x : random.choice([0,1])

    x = [map(rand,range(l)) for i in range(n)]
    y = map(rotL, x)

    return zip(x,y)

def sigmoid(x):
    return 1.0/(1 + math.exp(-x))

class NN:
    def __init__(self,ll,lr = 0.05):
        self.ll = ll
        self.lr = lr
        self.w, self.b = self.genWB()

    def genWB(self):
        ll = self.ll

        w = [np.random.randn(nin,nout) for (nin,nout) in zip(ll[:-1],ll[1:])]
        b = [np.random.randn(nout,1)   for nout       in            ll[1:]]
        return w,b

    def ff(self,x):
        v  = [None for i in self.ll]
        vf = [None for i in self.ll]

        f  = np.vectorize(sigmoid)

        v[0]  = x
        vf[0] = x

        for i in range(len(self.w)):
            v[i+1]  = np.dot(np.transpose(self.w[i]), v[i]) + self.b[i]
            vf[i+1] = f(v[i+1])

        return v,vf

    def fb(self,v,vf,y):
        f  = np.vectorize(sigmoid)
        df = lambda x: (1 - f(x))* f(x)

        w = self.w
        grad  = [None for i in range(len(w))]
        gradw = [None for i in range(len(w))]
        gradb = [None for i in range(len(w))]

        grad[-1] = (vf[-1] - y)*df(v[-1])

        for i in range(len(w)-2, -1,-1):
            grad[i] = np.multiply(np.dot(w[i+1],grad[i+1]),df(v[i+1]))

        gradb = grad

        for i in range(len(w)-1, -1,-1):
            gradw[i] = np.transpose(np.outer(grad[i], v[i]))
            #print i, gradw[i] ,v[i+1], grad[i]

        return gradw, gradb

    def trainStep(self,x,y):
        v,vf  = self.ff(x)
        yN    = vf[-1]

        e1    = self.err(yN,y)

        gw,gb = self.fb(v,vf,y)

        gw     = map(lambda x:np.multiply(x, self.lr), gw)
        gb     = map(lambda x:np.multiply(x, self.lr), gb)

        self.w = map(lambda x: x[0] - x[1], zip(self.w,gw))
        self.b = map(lambda x: x[0] - x[1], zip(self.b,gb))

        v2,vf2  = self.ff(x)
        e2    = self.err(vf2[-1],y)
        return [e1,e2]

    def err(self,yN,y):
        return math.sqrt(sum((yN - y ) ** 2))

    def train(self,data):
        cost   = []
        tcost  = []
        cnt    = 0
        maxcnt = len(data)/100

        for x,y in data:
            [e1,e2] = self.trainStep(x,y)
            tcost += [e2]
            cnt += 1
            if maxcnt == 0 or cnt % maxcnt == 0:

                cost += [sum(tcost)/len(tcost)]
                tcost = []
        return cost

    def normF(self,x):
        return x.reshape(1,len(x))[0]

    def test(self, data):
        for x,y in data:
            v,vf = self.ff(x)
            yn   = vf[-1]

            e = self.err(yn,y)

            print "x = {}, y = {}, out = {}, e = {}".format(self.normF(x),self.normF(y),self.normF(yn),e)






dat = genDat(10000,3)

LRs    = [0.01, 0.02, 0.05, 0.10, 0.15, 0.2, 0.3, 0.5, 0.9]
layers = [[3,2,3], [3,5,3], [3,4,4,3]]

datR = []
for x,y in dat:
    x = np.array(x).reshape(len(x),1)
    y = np.array(y).reshape(len(y),1)
    datR += [(x,y)]

for ll in layers:
    for lr in LRs:
        print "\nll = {}, lr = {}".format(ll, lr)
        nn = NN(ll,lr)

        #for x,y in datR:
        #    v,vf = nn.ff(x)
        #    nn.fb(v,vf,y)
        #    nn.trainStep(x,y)

        print "errors:",nn.train(datR)
        nn.test(datR[:5])
