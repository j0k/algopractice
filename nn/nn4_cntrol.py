# take attention on
# https://stackoverflow.com/questions/35032685/numpy-valueerror-shapes-not-aligned
#
#  especially:
#  def feedforward(self, a):
#        """Return the output of the network if ``a`` is input."""
#        for b, w in zip(self.biases, self.weights):
#            a = sigmoid(np.dot(w, a)+b)
#        return a

# start at about 16:00 15.10.2017
import random
import math
import numpy as np

def genData(n, l):
    rotL = lambda x: x[1:] + [x[0]]
    rotR = lambda x: [x[-1]] + x[:-1]

    ctrl = random.choice([0,1])

    randv = lambda : map(lambda r: random.choice([0,1]), range(l))

    def gen(s):
        ctrl = s[0]
        seq  = s[1:]
        seq2 = rotL(seq) if ctrl == 0 else rotR(seq)

        return [ctrl] + seq2

    x = [[random.choice([0,1])] + randv() for i in range(n)]
    y = map(gen, x)

    return zip(x,y)

def sigmoid(x):
    return 1.0/(1 + math.exp(-x))

class NN:
    def __init__(self,ll, LR = 0.05):
        self.ll = ll
        self.LR = LR
        self.w, self.b = self.genWB()

    def genWB(self):
        w = [np.random.randn(ni,no) for ni,no in zip(ll[:-1], ll[1:])]
        b = [np.random.randn(ni,1)  for ni    in ll[1:]]
        return w,b

    def ff(self,x):
        v  = [np.zeros(n) for n in self.ll]
        vf = [np.zeros(n) for n in self.ll]

        v[0]  = np.transpose([x])
        vf[0] = np.transpose([x])

        w = self.w
        b = self.b
        f = np.vectorize(sigmoid)
        for i in range(len(self.w)):
            v[i+1]  = np.dot(np.transpose(w[i]), v[i]) + b[i]
            vf[i+1] = f(v[i+1])

        return v,vf

    def fb(self,v,vf,x,y):
        f  = np.vectorize(sigmoid)
        df = np.vectorize( lambda x: (1 - f(x)) * f(x))

        w = self.w
        b = self.b

        grad  = [None for l in range(len(w))]
        gradw = [None for l in range(len(w))]
        gradb = [None for l in range(len(w))]

        #print vf[-1]
        grad[-1] = (vf[-1] - np.array(np.transpose([y]))) * df(v[-1])
        #print "GRAD-1", grad[-1]


        #print "w",w
        #print "v",v
        for i in range(len(grad) - 2,-1,-1):
            #print i

            #print "gi_1", grad[i+1]
            #print "w", w[i+1]
            #print "dot", np.transpose( np.dot(w[i+1], grad[i+1]) )

            fvi2 =  df( v[i+1])
            #print "df(v[i+1])",fvi2
            grad[i] =  np.multiply(np.dot(w[i+1], grad[i+1]), fvi2)

        for i in range(len(grad)-1,-1,-1):
            #print i
            #print "grad", grad
            #print "vf[i+1]",vf[i]
            #print np.transpose(vf[i+1])[0]
            #print np.transpose(vf[i+1])
            gradw[i] = np.outer(grad[i], vf[i])
            #print "Wi", w[i]
            #print "gradw[i]",gradw[i]

            # TODO: understand the start connection between vf[i] & w[i]

        gradb = grad

        return gradw, gradb

    def trainStep(self,x,y):
        v, vf  = self.ff(x)
        gw, gb = self.fb(v,vf,x,y)

        gw = map(np.transpose,gw)

        #print "W",self.w
        #print "gw",gw
        LR = self.LR
        gw = map(lambda x:x*self.LR, gw)
        self.w = map(lambda x: x[0]-x[1], zip(self.w, gw))
        self.b = np.array(self.b) - np.array(gb) * self.LR
        #print vf[-1], y
        return self.err(np.transpose(vf[-1])[0],y)
        #print "npa gw", np.array(gw)
        #print "gw",( np.array(gw) * self.LR)
        #self.w = self.w - np.multiply(gw, self.LR)

    def err(self, yN, y):
        return math.sqrt(sum((yN - y) ** 2))

    def train(self, data):
        cost  = []
        tcost = 0
        cnt   = 0
        maxCnt = int(len(data)/20)

        for x,y in data:
            x = np.array(x)
            y = np.array(y)

            tcost += nn.trainStep(x,y)

            cnt += 1
            if maxCnt == 0 or cnt % maxCnt == 0:
                cost += [tcost]
                tcost = 0


        return cost

    def test(self, data):
        for x,y in data:
            x = np.array(x)
            y = np.array(y)

            v,vf = self.ff(x)
            yN   = np.transpose(vf[-1])[0]
            err  = self.err(yN,y)

            print "TEST"
            print "x  = {}".format(x)
            print "y  = {}".format(y)
            print "yN = {}".format(np.transpose(vf[-1])[0])
            print "e  = {}".format(err)

    def avgerr(self,data):
        e = 0
        for x,y in data:
            x = np.array(x)
            y = np.array(y)

            v,vf = self.ff(x)
            yN   = np.transpose(vf[-1])[0]
            err  = self.err(yN,y)
            e += err
        print "avg error  = {}".format(e)



layers = [[4,3,4], [4,5,4], [4,6,4], [4,4,4,4], [4,5,5,4],[4,6,5,5,4]]
dat = genData(100000,3)
print dat[:10]
for ll in layers:
    print "ll:",ll
    nn = NN(ll)
    nn.avgerr(dat)
    for x,y in dat:
        x = np.array(x)
        y = np.array(y)

        v,vf = nn.ff(x)
        nn.fb(v,vf,x,y)

        nn.trainStep(x,y)

    print nn.train(dat)
    nn.test(dat[:10])
    nn.avgerr(dat)
    #print nn.w
    #print nn.b
