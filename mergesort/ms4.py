# 24.06.2017 18:58

def merge(aa):
    ll = sum(map(len,aa))
    li = 0

    inds = [0,0]
    c = []
    while sum(inds) < ll:
        flag = False
        for i in range(2):
            if not flag and inds[i] == len(aa[i]):
                j =  (i+1) % 2
                c += [ aa[j][inds[ j ]] ]
                inds[ j] += 1
                flag = True
                continue

        if not flag:
            ind = 1-int(aa[0][inds[0]] <= aa[1][inds[1]])
            c += [aa[int(ind)][inds[ind]]]
            inds[ind] +=1

    return c # i forgor to return it

def mergesort(a):
    if len(a)<=1:
        return a

    p = int(len(a)/2)
    aa = map(mergesort, [a[:p],a[p:]])
    return merge(aa)

A = [1,2,34,4,5,6,7,3,32,4,5,5,5,55,-453,345,3,2,-1]

print mergesort(A)

#
# block (all expr if flag == True):
#    exor1
#    expr2
#    expr3
#    expr4
#

# ==
