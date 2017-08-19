# 03.07.2017 17:41
# end 17:46

def merge(a,b):
    i = j = 0

    c = []
    while (i+j) < len(a) + len(b):
        if i == len(a):
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
    if len(a)<=1:
        return a
    p = int(len(a)/2)

    return merge(msort(a[:p]), msort(a[p:]))


A = [1,3,50,6,7,7,8,4,5,6,-4,4,-5,5,-5,5,0]

print msort(A)

#
# how to write this code in associative ML form
# msort(a):
#   len(a)<=0: a
#   return msort merge left right subpart of a
#
# merge(a,b):
#    merge lists a,b into one
#    order a[i]<=b[j]: a[i]; b[j]
#
# How to parse such constructions?
#

#
# L,R = a[:p],a[p:] == a[1/2, 1/2]
# [A1,A2,A3] = a[1/3, 1/3, 1/3]
# array splitting . how we can use it?
#
