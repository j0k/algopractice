# start: 19.10.2017, 14:32
# end: 15:36
# total time: 1h 4m

import random
import numpy as np
import math

np.set_printoptions(precision = 2, suppress = True)

def genData(n,l):
    rotL = lambda x: x[1:] + [x[0]]
    cmp  = lambda x: x + [1 if x[0]>x[1] else 0]

    rand = lambda x: map(lambda y: random.choice([0,1]), range(l))

    x = map(rand, range(n))
    y = map(lambda x: cmp(rotL(x)), x)

    return zip(x,y)

def toVVec(v):
    return np.array(v).reshape(len(v),1)

def normData(data):
    dat = []
    for (x,y) in data:
        dat += [(toVVec(x), toVVec(y))]

    return dat

def sigmoid(z):
    return 1.0/(1 + math.exp(-z))

class NN:
    def __init__(self,ll,LR = 0.05):
        self.ll = ll
        self.LR = LR
        self.w, self.b = self.genWB()

    def genWB(self):
        ll = self.ll
        w = [np.random.randn(nin,nout) for (nin, nout) in zip(ll[:-1], ll[1:])]
        b = [np.random.randn(nout,1)   for nout        in ll[1:]]

        return w,b

    def ff(self,x):
        f  = np.vectorize(sigmoid)
        v  = [None for l in self.ll]
        vf = [None for l in self.ll]

        vf[0] = v[0] = x


        w,b = self.w, self.b
        for i in range(len(w)):
            v[i+1]  = np.dot(np.transpose(w[i]),v[i]) + b[i]
            vf[i+1] = f(v[i+1])

        # is it right that vf[0] never used
        return v,vf

    def fb(self,v,vf,y):
        f  = np.vectorize(sigmoid)
        df = lambda x: (1 - f(x))*f(x)

        w  = self.w
        g  = [None for wi in w]
        gw = [None for wi in w]

        g[-1] = (vf[-1] - y)*df(v[-1])

        for i in range(len(w) - 2, -1,-1):
            g[i] = np.multiply(np.dot(w[i+1], g[i+1]), df(v[i+1]))

        for i in range(len(w) - 1, -1,-1):
            gw[i] = np.transpose(np.outer(g[i],v[i]))

        gb = g

        return gw, gb

    def trainStep(self,x,y):
        v,vf  = self.ff(x)
        gw,gb = self.fb(v,vf,y)

        mult = lambda y: map(lambda x: np.multiply(x,self.LR), y)
        gw = mult(gw)
        gb = mult(gb)

        div  = lambda x: x[0] - x[1]

        self.w = map(div,zip(self.w,gw))
        self.b = map(div,zip(self.b,gb))

        v2,vf2  = self.ff(x)

        e1 = self.err(vf[-1], y)
        e2 = self.err(vf2[-1],y)

        return [e1,e2]


    def err(self, yout, y):
        return math.sqrt(sum((yout - y) ** 2))

    def todo(self, data, f):
        return [f(x,y) for (x,y) in data]

    def train(self, data):
        return self.todo(data, self.trainStep)

    def trainPrint(self, data):
        errs    = map(lambda x: x[1], self.train(data))
        lenpart = 10
        n       = int(len(data)/lenpart)

        errs = [errs[p1:p2] for (p1,p2) in zip(range(0,len(data),n), range(n,len(data),n) )]
        errs = map(lambda x:sum(x)/len(x), errs)

        return errs

    def test(self, data):
        res = self.todo(data, lambda x,y: self.ff(x))
        for i,r in enumerate(res):
            out = r[1][-1]
            x,y = data[i]
            e = self.err(out,y)
            print "x = {}, y = {}, out = {}, e = {}".format(nf(x), nf(y), nf(out), e)

def nf(v):
    return v.reshape(len(v))

layers = [[3,3,4], [3,5,4], [3, 7, 4]]

dat = genData(10000,3)
dat = normData(dat)

#print dat
for ll in layers:
    print "ll = {}".format(ll)
    nn = NN(ll)
    for (x,y) in dat:
        v,vf  = nn.ff(x)
        gw,gb = nn.fb(v,vf,y)
        #print nn.trainStep(x,y)

    #nn.train(dat)
    #nn.test(dat[:5])
    print nn.trainPrint(dat)
    nn.test(dat[:10])
