class Maxing:
    def __init__(self,e):
        self.seq = [e]
        self.d = 0
        self.t = 1

    def add(_, e):
        seq = _.seq
        if (len(seq) == 0) or _.go_t(e):
            _.seq += [e]

    def free(_):
        _.seq = []

    def add_f(_, elems):
        _.seq += elems


    def go_t(_,e):
        return (seq[-1]<e and _.t==1) or (seq[-1]>e and _.t==-1)


    def dist(self):
        return max(self.seq) - min(self.seq)


def maxseq(a):
    if len(a)<=1:
        return 0

    s = [Maxing(a[0]), Maxing(a[0])]

    b = 0
    for i,e in enumerate(a):
        if e == el:
            continue
        if s[b].go_t(e):
            s[b].add(e)
        else:
            b = 1 - b
            s[b].free()
            s[b].add_f([e,el])

        ds = map(lambda x:x.dist(), s)
        if ds[0] > ds[1]:
            
