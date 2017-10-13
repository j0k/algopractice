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

def transpose(m):
    w = len(m)
    h = len(m[0])

    m2 = [[0 for j in range(w)] for i in range(h)]

    for i in range(w):
        for j in range(h):
            m2[j][i] = m[i][j]

    return m2

class NN:
    def __init__(self, ll):
        self.LR    = 0.05
        self.tcost = 0
        self.ll    = ll

        self.tcost = 0
        self.cost  = []
        self.cnt   = 0

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

                    V[i+1][iOut] += w[i][iIn][iOut] * VF[i][iIn]

                    #if i == 0:
                    #    # print i, iIn, x
                    #    V[i+1][iOut] += w[i][iIn][iOut] * V[i][iIn]
                    #else:
                    #    V[i+1][iOut] += w[i][iIn][iOut] * VF[i][iIn]
                        #V[i+1][iOut] += w[i][iIn][iOut] * (VF[i][iIn] + b[i][iOut])

                V[i+1][iOut]  += b[i][iOut]

            # Table[{zz[[i]], aa[[i]]} = {t = (w[[i]].If[i === 1, x, aa[[i - 1]]] + b[[i]]), LogisticSigmoid[t]}, {i, 1, len}];
            # sum with b before *w[[i   ]]

            for iOut in range(nout):
                VF[i+1][iOut]  = f(V[i+1][iOut])

        return V, VF

    def fb(self,a,z,x,y,w):
        # vf = a
        # v  = z
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
        #print "a",a[nl-1], a[-1]
        #print "y",y
        grad[nl-1] = (toA(a[nl]) - toA(y)) * vdf (toA(z[nl]))
        grad[nl-1] = np.reshape(grad[nl-1],[ len(grad[nl-1]),1])
        #print "grad[{}] = {}".format(nl-1, grad[nl-1])
        #Do[Delta[[i]] = (Transpose[w[[i + 1]]].Delta[[i + 1]])*Sigma[z[[i]]], {i, len - 1, 1, -1}];(*subsequent backpropagation steps*)

        # TODO: Understand the sense of that operations
        # for AML: Feel the sense of everything! slogan

        for i in range(nl-2,-1,-1):
            # print "i",    i
            wt =   w[i + 1]

            # here I lost the transpose operation
            # TODO: find it!

            #print "wt",    wt
            #print "grad[{}] = {}".format(i+1, grad[nl-1])
            #print 'grad[i+1]',grad[i+1]
            grad0 = np.reshape(grad[i+1], [len(grad[i+1]),1])
            #print "grad", grad0

            #w0 = [[ 0.42927229,  0.87054113 , 0.10954286,  0.32397304,  0.15731477],
            #      [ 0.1060979 ,  0.3795275 ,  0.32137433 , 0.72440216 , 0.51629504],
            #      [ 0.07480367 , 0.76149711 , 0.50841416 , 0.79733426 , 0.12691061]]
            #w0 = w[i + 1]
            #grad0 = [ 0.1439525 ,  0.13764996 , 0.0245685 ]
            #print "vdf z[i  ]", vdf (z[i])
            #print "vdf z[i+1]", vdf (z[i+1])
            #grad[i] = np.dot(wt, grad0)
            #print "grad[i]", grad[i]

            grad[i] = np.multiply( np.dot(wt, grad0),  np.transpose([vdf (z[i+1])]))
            #print "grad[{}] = {}".format(i, grad[i])
            #print "grad[i]", grad[i]
            #grad0 = np.reshape(grad[i+1], [len(grad[i+1]),1])
            #np.dot(wt, grad0)

        # Do[gradw[[i]] = Outer[Times, Delta[[i]], a[[i - 1]]], {i, len, 2, -1}];(*weight gradients, except final one*)
        for i in range(nl-1,-1,-1):
            gradw[i] = np.outer(grad[i], a[i])
            #print "gradw[i]",gradw[i]

        gradb = grad

        #print "gradB", gradb
        return gradw, gradb


    def nn(self, data):
        cnt   = int(len(data)/20)
        self.cost  = []
        tcnt  = 0
        tcost = 0

        for x,y in data:
            v,vf = self.pure_ff(x, nn.W, nn.B)

            diff = np.array(y) - vf[-1]
            tcost += 0.5 * math.sqrt(sum(map(lambda x:x ** 2, diff))) ** 2
            #print tcost
            tcnt += 1
            if tcnt % cnt == 0:
                tcnt  = 0
                self.cost += [tcost]
                tcost = 0

            gradw, gradb = self.fb(vf,v,x,y,nn.W)

            #print "w", nn.W
            gradw = map(np.transpose, gradw)
            #print "gradb",   gradb
            gradb = map(np.transpose, gradb)
            gradb = map(lambda x:x[0], gradb)

            #print "self.B",  np.array(self.B)
            #print "gradb",   np.array(gradb)
            #print "self.LR", self.LR

            #gradb = np.array(self.B) * self.LR
            #print "gradw", gradw
            self.W = np.array(self.W) - np.array(gradw) * self.LR
            #print "SELF.B 1", self.B
            #print "np.array(gradb)",np.array(self.B) - np.array(gradb) * self.LR
            self.B = np.array(self.B) - np.array(gradb) * self.LR
            self.B = map(np.transpose, self.B)
            #print "SELF.B 2", self.B

    def test(self, data):
        for x,y in data:
            v,vf = self.pure_ff(x, nn.W, nn.B)
            diff = np.array(y) - vf[-1]
            tcost = 0.5 * math.sqrt(sum(map(lambda x:x ** 2, diff))) ** 2
            print "X", x
            print "Y", y
            print "vf", vf[-1],
            print "err", tcost


layers = [[3,3,3], [3,5,3], [3,5,2,5,3], [3,1,3], [3,2,1,2,3], [3,6,5,4,3]]

data    = genData(10000,3)

def data2dat(data):
    dat = []
    for i in range(len(data[0])):
        x = data[0][i]
        y = data[1][i]
        dat += [[x,y]]

    return dat

dat = data2dat(data)

d0 = data[0][0]
r0 = data[1][0]
print "d0",d0
print "r0",r0


for ll in layers:
    print "layers:", ll
    nn = NN(ll)
    nn.genWB()
    v, vf = nn.pure_ff(d0, nn.W, nn.B) # zz,aa
    nn.fb(vf, v, d0, r0, nn.W)

    nn.nn(dat)
    nn.test(dat[:3])
    print nn.cost


    #print nn.pure_ff(d0,nn.W,nn.B)

print "GREAT TEST OF LONG NET", ll

data    = genData(1000000,3)
dat     = data2dat(data)
ll  = [3,6,5,4,3]
nn = NN(ll)
nn.genWB()
nn.nn(dat)
nn.test(dat[:10])
print nn.cost

#print data
nn.genWB()
#print nn.genWB()
d0 = data[0][0]
#print nn.ll
#print nn.pure_ff(d0,nn.W,nn.B)
