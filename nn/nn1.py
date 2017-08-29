# data set
import random

rand01 = lambda x : random.choice([0,1])
rotateL = lambda x: x[1:] + [x[0]]
data = [map(rand01, range(3)) for i in range(10)]

data = map(lambda x:[x, rotateL(x)],data)
print data



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
