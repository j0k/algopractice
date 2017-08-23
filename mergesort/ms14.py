# merge sort

def merge(a,b):
    i,j = 0,0
    # opt = [[],[]]
    c = []
    while i + j < len(a) + len(b):
        if i == len(a):
            c += [b[j]]
            j += 1
        elif j == len(b):
            c += [a[i]]
            i +=  1
        else:
            if a[i] < b[j]:
                c += [a[i]]
                i += 1
            else:
                c += [b[j]]
                j += 1

    return c

def msort(a):
    p = int(len(a)/2)
    return a if p == 0 else merge(msort(a[:p]), msort(a[p:]))

A = [1,2,3,1,2,3,-3,-2,1,0,0,0,100,-100,1234,0,2,3,-4,-5]

print(msort(A))

# def merge(a,b)
#   i,j = 0,0
#   c = []
#   change(&arr, &ind): c += [arr[ind]]; ind ++
#
#   while i + j < +/ len @ (a,b):
#     when:
#        i == len(a) => change(a,i)
#        j == len(b) => change(b,j)
#        a[i] < b[j]: change(a,i) ? change(b,j)
#
#    return c
#
#   better way:
#   alias: a.i = i,
#          b.i = j
#
#   change(&arr): c += [arr[.i]]; arr.i ++
#   while i + j < +/ len @ (a,b):
#     when:
#        i == len(a) => change(a)
#        j == len(b) => change(b)
#        a[i] < b[j]: change(a) ? change(b)
#
#    return c
