# 14.10.2017
# starting at about 13:00
# CardPay office

import random
import numpy as np
import math

def sigmoid(x):
    return 1.0/(1+math.exp(-x))

def genData(n, length):
    rotL = lambda x: x[1:] + [x[0]]

    rand = lambda x: map(lambda y: random.choice([0,1]),range(x))

    dat = []
    for i in range(n):
        x = rand(length)
        y = rotL(x)
        dat += [ [x,y] ]

    return dat

class NN:
    def __init__(self, ll, LR = 0.05):
        self.LR = LR
        self.ll = ll
        self.W, self.B = self.genWB()

    def genWB(self):
        ll = self.ll
        W = []
        B = []

        for i in range(len(ll) - 1):
            l1 = ll[i]
            l2 = ll[i+1]

            B.append( [(1 - random.random() * 2) for k in range(l2)] )
            W.append( [[(1 - random.random() * 2) for k in range(l2)] for l in range(l1) ] )

        return np.array(W), np.array(B)

    def ff_pure(self, x):
        # return v, vf
        f = lambda x: sigmoid(x)


        V  = [[0 for j in range(self.ll[i])] for i in range(len(self.ll))]
        VF = [[0 for j in range(self.ll[i])] for i in range(len(self.ll))]

        V[0] = VF[0] = x

        W = self.W
        B = self.B

        for i in range(len(W)):
            inN = len(W[i])
            ouN = len(W[i][0])

            for iN in range(inN):
                for oN in range(ouN):
                    V[i+1][oN] += W[i][iN][oN] * VF[i][iN]

            for oN in range(ouN):
                V[i+1][oN] += B[i][oN]
            # fix: first forget this BLOCK with adding B

            for oN in range(ouN):
                VF[i+1][oN] = f(V[i+1][oN])
                # fix: I made an error VF instead of V

        return np.array(V), np.array(VF)

    def fb(self,V,VF,x,y):
        f   = lambda x: sigmoid(x)
        df  = lambda x: (1 - sigmoid(x)) * sigmoid(x)

        vf  = np.vectorize(f)
        vdf = np.vectorize(df)

        W = self.W
        B = self.B

        nl = len(W)
        # ERROR
        # gradb = gradw = grad = [None for i in range(nl)]

        gradw = [None for i in range(nl)]
        gradb = [None for i in range(nl)]
        grad  = [None for i in range(nl)]

        grad[-1] = (VF[-1] - y) * vdf(V[-1])
        #print "last",grad[nl-1]
        # Do[Delta[[i]] = (Transpose[w[[i + 1]]].Delta[[i + 1]])*
        #    Sigma[z[[i]]], {i, len - 1,  1, -1}];(*subsequent backpropagation steps*)

        for i in range(nl-2,-1,-1):
            grad[i] = np.multiply( np.dot(W[i+1], grad[i+1]) , vdf(V[i+1]))
            # print "1" ,grad[i]
            # grad[i] = np.dot(W[i+1], grad[i+1]) * vdf(V[i+1])
            # print "0" ,grad[i]

        # Do[gradw[[i]] = Outer[Times, Delta[[i]], a[[i - 1]]], {i, len, 2, -1}];
        # (*weight gradients, except final one*)

        for i in range(nl-1,-1,-1):
            gradw[i] = np.outer(grad[i], VF[i])
        gradb = grad

        return gradw, gradb, grad

    def learnStep(self,x,y):
        v, vf      = self.ff_pure(x)
        gw, gb, gg = self.fb(v,vf,x,y)

        gw = map(np.transpose, gw) # fix it!
        gb = map(np.transpose, gb) # fix it!

        self.W = self.W - np.multiply(gw, self.LR)
        self.B = self.B - np.multiply(gb, self.LR)

        err = self.err(vf[-1], y)
        return v,vf,err

    def err(self,yn,y): #y Neuron
        return math.sqrt(sum((y - yn) ** 2))

    def train(self,data):
        tcost, cost = 0, []
        max_cnt = 0 + int(len(data)/10)
        cnt = 0

        for x,y in data:
            x = np.array(x)
            y = np.array(y)
            #print x,y
            v,vf,err = self.learnStep(x,y)

            tcost += err

            cnt += 1
            if max_cnt == 0 or cnt % max_cnt == 0:
                cost += [tcost]
                tcost = 0

        return cost

    def test(self,data):
        for x,y in data:
            x = np.array(x)
            y = np.array(y)

            v,vf = self.ff_pure(x)
            yN   = vf[-1]
            err  = self.err(yN,y)
            yR   = map(round,yN)

            print "x   = {}, y  = {}".format(x,y)
            print "yN  = {}, yR = {}".format(yN,yR)
            print "err = {}".format(err)


dat = genData(100000,3)
layers = [ [3,1,3], [3,3,3], [3,5,3], [3,4,2,6,3] ]

for ll in layers:
    print "ll:", ll
    nn = NN(ll)
    for x,y in dat:
        x = np.array(x)
        y = np.array(y)

        v,  vf = nn.ff_pure(x)
        gw, gb, gg = nn.fb(v,vf,x,y)
        nn.learnStep(x,y)

    cost = nn.train(dat)
    print cost
    nn.test(dat[:5])
