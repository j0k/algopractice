# 27.06.2017

def qs(a):

    l = len(a)
    if l<=1:
        return a

    p = int(l/2)
    ep = a[p]
    b = [[],[]]
    for i in range(l):
        if i == p:
            continue
        else:
            e = a[i]
            b[e <= ep] += [e]
    return qs(b[1]) + [ep] + qs(b[0])

A = [-10,-100,3,4,5,6,17,2320,3,3,3,3,3,0]

print qs(A)

#
# too long code
# qsort is very simple
# qsort(A):
#    L,R = A[^p](<=,> m) /. m,p = A[p], int(len(A)/2)
#    ret self(L),[m],self(R)

# evaluated dependent code chains paradigm
# a[x1_, x2_] = 30 /. x1 = x2 ^ 2 + 100, x2 = 1000
# a[x1_, x2_] = 30 /. x1 = 100, x2 = 1000 + x1

# [1,2,3,4,5,6,7].between(each[_e1,_e2] insert x)
# [1,x,2,x,3,x,4,x,5,x,6,x,7]
# _connected with type/pattern matching

# AML - Abstract Macro Language
#
# compiler of AML will have to be written in AML.
#
