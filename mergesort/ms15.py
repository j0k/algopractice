import random

def randpermute(a):
    for i in range(len(a)):
        p = int(random.random() * len(a))
        c = a[p]
        a[p] = a[i]
        a[i] = c

    return a

# it would be useful to have common version to merge (a,b), (a,b,c), (a,b,c,d)
def merge(a,b):
    #i, j = 0,0
    c = []
    arrs = [a,b]
    inds = [0,0]

    def change(ind):
        i = inds[ind]
        c.append(arrs[ind][i])        
        inds[ind] += 1

    while sum(inds) < len(a) + len(b):
        i,j = inds # how to simplify it
        if i == len(a):
            change(1)
        elif j == len(b):
            change(0)
        elif a[i] <= b[j]:
            change(0)
        else:
            change(1)

    return c

def msort(a):
    p = int(len(a) * random.random())
    return merge(msort(a[:p]), msort(a[p:])) if len(a) > 1 else a

A = randpermute(range(10))
print(A)
print(msort(A))

#print(merge([1,2],[2,3]))
