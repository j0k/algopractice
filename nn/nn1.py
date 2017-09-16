# data set
import random

rand01 = lambda x : random.choice([0,1])
rotateL = lambda x: x[1:] + [x[0]]
data = [map(rand01, range(3)) for i in range(10)]

data = map(lambda x:[x, rotateL(x)],data)
#print data

import random

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
        l = len(w)

        f = lambda x: x * 2

        AA,ZZ = [], []
        aa,zz = [], []
        for i in range(l):
            n = len(w[i])
            if i == 0:
                rj = []
                for j in range(n):
                    rj += [ w[i][j] * d[j] ]

                rj = sum(rj)






        pass

    def fb(self):
        pass

nn = NN([1,2,2,1],data)
print nn.genW()
print nn.genB()

#
# NeuralNetwork[layers_List, data_] :=
#   Module[{len, w, b, \[Lambda], d\[Sigma], y, z, a, \[Delta], gradw,
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
