import random
import math
import numpy as np

def sigmoid(x):
    return 1/(1 + math.exp(-x))

def genData(n, len):

    rotateL =  lambda x: x[1:] + [x[0]]
    rotateR =  lambda x: [x[-1]] + x[:-1]

    d  = [[random.choice([0,1]) for j in range(len)] for i in range(n)]
    d2 = map(rotateL,d)

    return [d,d2]


class NN:
    def __init__(self, ll):
        self.LR    = 0.05
        self.tcost = 0
        self.ll    = ll

    def genWB(self,ll = None):
        if ll == None:
            ll = self.ll

        W = []
        for i in range(len(ll)-1):
            n,k = ll[i:i+2]

            w = [[random.random() for x1 in range(k)] for x2 in range(n)]
            W += [w]


        B = [[random.random() for j in range(ll[i])] for i in range(1,len(ll))]

        self.W = W
        self.B = B
        return [self.W, self.B]

    def bp():
        # backpropagation
        pass

    def ff():
        pass

    def pure_ff(self,x,w,b):
        f = lambda x: sigmoid(x)
        aa = []
        V = [[0 for i in range(self.ll[l])] for l in range(len(self.ll))]
        V[0] = x

        VF = [[0 for i in range(self.ll[l])] for l in range(len(self.ll))]
        VF[0] = x
        # V = [[0]  for l in range(len(self.ll))]


        for i in range(len(w)):
            #print "w", (len(w))
            nin  = len(w[i])
            nout = len(w[i][0])

            #print nin,nout

            for iIn in range(nin):
                for iOut in range(nout):
                    # print iIn, iOut, w[i]
                    if i == 0:
                        # print i, iIn, x
                        V[i+1][iOut] += w[i][iIn][iOut] * V[i][iIn]
                    else:
                        V[i+1][iOut] += w[i][iIn][iOut] * VF[i][iIn]
                        #V[i+1][iOut] += w[i][iIn][iOut] * (VF[i][iIn] + b[i][iOut])

                V[i+1][iOut]  += b[i][iOut]

            # Table[{zz[[i]], aa[[i]]} = {t = (w[[i]].If[i === 1, x, aa[[i - 1]]] + b[[i]]), LogisticSigmoid[t]}, {i, 1, len}];
            # sum with b before *w[[i   ]]

            for iOut in range(nout):
                VF[i+1][iOut]  = f(V[i+1][iOut])

        return V, VF

    def fb(self,a,z,x,y,w):
        f   = lambda x: sigmoid(x)
        df  = lambda x: (1 - sigmoid(x)) * sigmoid(x)
        vf  = np.vectorize(f)
        vdf = np.vectorize(df)


        toA = np.array

        delta = [[] for i in range(len(w))]

        gradw, gradb = 0,0

        nl    = len(w)
        grad  = [None for i in range(nl)]
        gradw = [None for i in range(nl)]
        gradb = [None for i in range(nl)]

        # initial backpropagation step
        print "a",a[nl-1], a[-1]
        print "y",y
        grad[nl-1] = (toA(a[nl]) - toA(y)) * vdf (toA(z[nl]))


        return gradw, gradb


    def nn():
        pass

layers = [[3,3,3],[3,5,3], [3,5,2,5,3], [3,1,3], [3,2,1,2,3], [3,6,5,4,3]]

data    = genData(10,3)
d0, r0  = data[0][0], data[1][0]

for ll in layers:
    print "layers:", ll
    nn = NN(ll)
    nn.genWB()
    v, vf = nn.pure_ff(d0, nn.W, nn.B) # zz,aa
    nn.fb(vf, v, d0, r0, nn.W)
    #print nn.pure_ff(d0,nn.W,nn.B)


#print data
nn.genWB()
#print nn.genWB()
d0 = data[0][0]
#print nn.ll
#print nn.pure_ff(d0,nn.W,nn.B)
