# 23.06.2017
# 12min, 1 error

A = [10,2,-4,3,3,3,100,1000,-999,1,2,3,4,5]

def msort(a):
    #l = len(a)
    #if l <= 1:
    #    return a

    m = int(len(a)/2);
    #L,R = msort(a[:m]),msort(a[m:])
    return merge(msort(a[:m]), msort(a[m:])) if len(a)>1 else a

def merge(a,b):
    c = []

    i = j = 0
    li = 0

    while li < len(a) + len(b):
        if i == len(a):
            c += [ b[j] ]
            j += 1
        elif j == len(b):
            c += [ a[i] ]
            i += 1
        else:
            if a[i] <= b[j]:
                c += [ a[i] ]
                i += 1
            else:
                c += [ b[j] ]
                j += 1

        li = i+j # error - ob the first time I don't forgot this

    return c

print msort(A)
