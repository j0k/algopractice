def merge(a,b):
    #print a,b
    if (len(a) + len(b)) == 0:
        return a+b

    i = j = 0
    c = []
    while (i+j) < len(a)+len(b):
        if i==len(a):
            c += [b[j]]
            j += 1
        elif j == len(b):
            c += [a[i]]
            i += 1
        else:
            if a[i] <= b[j]:
                c += [a[i]]
                i += 1
            else:
                c += [b[j]]
                j += 1
    return c

def msort(a):
    if len(a) <= 1:
        return a

    m = int(len(a)/2)
    return merge(msort(a[:m]), msort(a[m:]))

A = [1,2,4,4,56,3,2,2,5,3,0,-10,100,-100,0,0,0,4]

print msort(A)

#
#
# merge(a,b):
#   c: e in a+b, each e in a+b in c, i<=j: c[i] <= c[j]
#
# msort(a):
#   #a <= 1 ==> ret a
#   ret merge(it@a[:m],it@a[m:]) /. m->len(a)/2
#

# AML must be very easy for debugging language
#
# debugging is part of that language
# also because of In-Place execution paradigm
