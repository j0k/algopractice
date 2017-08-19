# 04.07.2017
# word IF if not usefull
# smth: do1() ? do2()
# smth: do1() ?
# smth2: do2()

def merge(a,b):
    i = j = 0
    c = []
    while i+j <= len(a) + len(b):
        if i == len(a):
            b += [c[j]]
            J += 1
        i==len(a) : b,c[j],j
        break

    return c

def msort(a):
    p = int(len(a)/2)

    return a if p==0 else merge(msort(a[:p]),msort(a[p:]))

A = [1,2,3]
A += [4] if True else [5]
merge(A,[])
print msort(A)


i = 5
def change(*i):
    i += 6

change(i)
print i
