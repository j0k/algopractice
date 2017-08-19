class bintree:
    def __init__(self,n=None):
        self.n = n

        self.L = None #bintree()
        self.R = None #bintree()


    def ins(self, bt):
        if self.n == None:
            self.n = bt.n
        else:
            if bt.n <= self.n:
                if self.L != None:
                    self.L.ins(bt)
                else:
                    self.L = bt
            else:
                if self.R != None:
                    self.R.ins(bt)
                else:
                    self.R = bt

    def getarray(self):
        L = [] if self.L == None else self.L.getarray()
        R = [] if self.R == None else self.R.getarray()
        return [] if self.n == None else (L + [self.n] + R)


A = [200000, -10000, 1,4,5,6,3,4,-3,0]
bA = map(bintree,A)

b0 = bintree(0);
map(lambda x:b0.ins(x), bA)

print b0.getarray()
