import random
import math

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
                        V[i+1][iOut] += w[i][iIn][iOut] * f(VF[i][iIn])

                V[i+1][iOut]  += self.B[i][iOut]

            for iOut in range(nout):
                VF[i+1][iOut]  = f(V[i+1][iOut])

        return V, VF

    def fb(self,a,z,x,y,w):
        df = lambda x: (1 - sigmoid(x)) * sigmoid(x)
        f  = lambda x: sigmoid(x)

        delta = [[] for i in range(len(w))]


    def nn():
        pass

layers = [[3,3,3],[3,5,3], [3,5,2,5,3], [3,1,3], [3,2,1,2,3], [3,6,5,4,3]]


data = genData(10,3)
d0 = data[0][0]

for ll in layers:
    print "layers:", ll
    nn = NN(ll)
    nn.genWB()
    nn.pure_ff(d0,nn.W,nn.B)
    print nn.pure_ff(d0,nn.W,nn.B)


#print data
nn.genWB()
#print nn.genWB()
d0 = data[0][0]
#print nn.ll
#print nn.pure_ff(d0,nn.W,nn.B)
