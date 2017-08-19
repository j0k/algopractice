# 05.07.2017

class BinTree:
    def __init__(self,n):
        self.n = n
        self.L = None
        self.R = None

    def printit(self):
        print self.n

    def to_array(self):
        def f(x):
            return [] if x == None else x.to_array()

        L = f(self.L)
        R = f(self.R)

        return L + [self.n] + R


    def insert(self,bt):
        def ins(obj,x,bt):
            if obj.x == None:
                obj.x = bt
            else:
                obj.x.insert(bt)

        if self.n <= bt.n:
            #ins(self,self.R,bt)
            if self.R == None:
                self.R = bt
            else:
                self.R.insert(bt)
        else:
            # ins(self,self.L,bt)
            if self.L == None:
                self.L = bt
            else:
                self.L.insert(bt)

A = [1,2,3,-4,3,4,5,5,2,-1,10]

b = BinTree(0)
for i in range(len(A)):
        b.insert(BinTree(A[i]))

print b.to_array()
