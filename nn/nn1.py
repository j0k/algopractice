# data set
import random

rand01 = lambda x : random.choice([0,1])
rotateL = lambda x: x[1:] + [x[0]]
data = [map(rand01, range(3)) for i in range(10)]

data = map(lambda x:[x, rotateL(x)],data)
#print data

import random
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# start at 16.09.2017
# step 1 end at 15:26
class NN:
    def __init__(self,ll,data):
        self.ll    = ll
        self.data  = data
        self.LR    = 0.05
        self.tcost = 0
        self.cost  = []

        self.cnt   = len(data)
        self.tcnt  = 0
        print ll
        pass

    def genW(self):
        W = []
        for i in range(len(self.ll)-1):
            j = i + 1

            [n1, n2] = self.ll[i:i+2]

            w1 = []
            for i1 in range(n1):
                w2 = []
                for i2 in range(n2):
                    w2 += [random.random()]
                w1 += [w2]
            W += [w1]

        return W

    def genB(self):
        B = []

        for i in range(1,len(self.ll)):
            bi = []
            for j in range(self.ll[i]):
                b = random.random()
                bi += [b]
            B += [bi]

        return B

    def ff(self, d, w, b):
        print d
        x,y = d
        l = len(w)

        f = lambda x: sigmoid(x)

        AA,ZZ = [], []
        aa,zz = [], []
        # print w
        # Table[{zz[[i]], aa[[i]]} = {t = (w[[i]].If[i === 1, x, aa[[i - 1]]] + b[[i]]),  LogisticSigmoid[t]}, {i, 1, len}];
        for i in range(len(w)):
            # i means connection layer
            nin   = len(w[i])
            nout  = len(w[i][0])

            print "nin=",nin," nout=",nout
            # neuron count out
            #WN2 = [[[] for i in range(nin)] for j in range(nout)]
            WN2 = [[] for j in range(nout)]

            for no in range(nout):
                wsum = 0
                for ni in range(nin):

                    if i == 0:
                        wsum += w[i][ni][no] * x[ni]
                    else:
                        wsum += w[i][ni][no] * aa[i-1][ni]

                if i != 0:
                    wsum += b[i][no]
                WN2[no] += [wsum]


            # for n in range(nc):
            #     wn = []
            #     print range(len(w[i][n]))
            #     for j in range(len(w[i][n])):
            #         #WN[j] +=
            #         if i == 0:
            #             wsum = 0
            #             for jj in range(len(x)):
            #                 wsum += w[i][n][jj] * x[jj]
            #             WN2[j] += [ wsum  ]
            #         else:
            #             print i,n,j, w[i][n][j]
            #             print "aa", aa[i-1]
            #             wsum = 0
            #             for jj in range(len(w[i-1][n])):
            #                 wsum += w[i][n][jj] * aa[i-1][jj]
            #             #wx = w[i][n][j] * aa[i-1][j]
            #             WN2[j] += [ wsum + b[i][j] ]
            #         #wn += [ w[i][n][j] * x[j] + b[i][j] ]#check b[i][j]

            calcV = []

            print "WN2:", WN2

            for n in range(nout):
                WN2[n] = sum(WN2[n])
                calcV += [ f(WN2[n]) ]

            zz += [WN2]
            aa += [calcV]

        return (zz, aa)

    # FeedBackward
    def fb(self,a,z,x,y,w):
        df = lambda x: (1 - sigmoid(x)) * sigmoid(x)

        delta = [[] for i in range(len(w))]

        #delta[len(w)] = (a[len(w)] - y) * df(z[len(w)])

        nlayers = len(w)
        nin  = len(w[-1][0])
        nout = len(w[-1])

        delta[-1] = [0 for i in range(nin)]
        for i in range(nin):
            # for the last layer
            #
            # print "n for lastL",len(w[-1])
            # print "a", a[-1]
            # print "y", y
            # print "z",z[-1]
            # print "delta", delta[-1]
            delta[-1][i] = (a[-1][i] - y[i]) * df(z[-1][i])

            #   FeedBackward[a_, z_, x_, y_, w_] :=
            #       Module[{len, dSigma, Delta, gradw, gradb},
            #
            #           len = Length[w];
            #           dSigma[zz_] := (1 - LogisticSigmoid[zz]) LogisticSigmoid[zz];(*derivative of the Sigma function*)
            #           Delta = gradw = gradb = ConstantArray[Null, {len}];
            #           Delta[[len]] = (a[[len]] - y)* dSigma[z[[len]]];(*initial backpropagation step*)
            #           Do[Delta[[i]] = (Transpose[w[[i + 1]]].Delta[[i + 1]])*dSigma[z[[i]]],
            #                                {i, len - 1, 1, -1}];(*subsequent backpropagation steps*)
            #           Do[gradw[[i]] = Outer[Times, Delta[[i]], a[[i - 1]]],
            #                                {i, len, 2, -1}];(*weight gradients, except final one*)
            #           gradw[[1]] = Outer[Times, Delta[[1]], x];(*final weight gradient*)
            #           gradb = Delta;(*bias gradient*)
            #           {gradw, gradb}
            #       ];
            # pass
        return 1


    def onestep(self, d):
        x,y = d
        w = self.genW();
        b = self.genB()
        z,a = nn.ff(d, w, b)
        self.fb(a,z,x,y, w)

nn = NN([3,5,3],data)
print nn.genW()
print nn.genB()
#print data[0]
#print nn.ff(data[0], nn.genW(), nn.genB())
print nn.onestep(data[0])
#
# NeuralNetwork[layers_List, data_] :=
#   Module[{len, w, b, \[Lambda], dSigma, y, z, a, Delta, gradw,
#     gradb, cost, tcost, cnt, tcnt, forward, x},
#    len = Length[layers];
#    w = Table[
#      RandomReal[1, {layers[[i]], layers[[i - 1]]}], {i, 2,
#       len}];(*init weights*)
#    b = Table[
#      RandomReal[1, {layers[[i]]}], {i, 2, len}];(*init biases*)
#    \[Lambda] = 0.05;(*learning rate*)
#    tcost = 0; cost = {};(*cost functions*)
#    cnt = Round[Length[data]/100]; tcnt = 0;(*cost iteration counters*)
#
#
#    Do[
#     {x, y} = d;
#     {z, a} = FeedForward[x, w, b];
#     tcost += 0.5*EuclideanDistance[y, a[[len - 1]]]^2;(*cost function*)
#
#
#     If[Mod[++tcnt, cnt] === 0, AppendTo[cost, tcost/cnt]; tcost = 0];
#     {gradw, gradb} = FeedBackward[a, z, x, y, w];
#     w = w - \[Lambda] gradw;(*update weights*)
#     b = b - \[Lambda] gradb;(*and biases*)
#     ,
#     {d, data}];
#    <|"w" -> w, "b" -> b, "cost" -> cost|>
#    ];

# constructed trainset

# implement NN
# 1. FeedForward
# 2. FeedBackward
# 3. NeuralNetwork (layers, data)

# aml
# rande01 = ?/ (0,1)

# Declarative aaml examples
# rotateL = [_a0 .. _an] -> [a1 .. an, a0]
# doesn't matter
# rotateL = [_a0 .. _an] -> [_a1 .. _an, _a0]

# rande01 /@ range(10)
# Number Picture AutoComplete
