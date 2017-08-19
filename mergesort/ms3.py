# 24.06.2017

def merge(aa):
    ll = sum(map(len,aa))
    li = i = j = 0

    inds = [0,0]
    c = []
    while li < ll:
        if i == len(aa[0]):
            c += [aa[1][j]]
            j += 1
        elif j == len(aa[1]):
            c += [aa[0][i]]
            i += 1
        else: # i write else in statement before and this forgot

            print aa,i,j
            ind = 1-int(aa[0][i] <= aa[1][j])

            if ind == 0:
                c += [aa[int(ind)][i]]
                i +=1
            else:
                c += [aa[int(ind)][j]]
                j += 1
        li = i+j
    return c # i forgor to return it

def mergesort(a):
    if len(a)<=1:
        return a

    p = int(len(a)/2)
    aa = map(mergesort, [a[:p],a[p:]])
    return merge(aa)

A = [1,2,34,4,5,6,7,3,32,4,5,5,5,55,-453,345,3,2,-1]

print mergesort(A)
