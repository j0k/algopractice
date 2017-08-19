
# this is interesting case
def min_pos(a,pos):
    if pos == len(a):
        return -1

    p = None
    mi = 100000
    for i in range(len(a)):
        if a[i] < mi:
            mi = a[i]
            p = i
    return p

def merge(aaa):
    ll = sum(map(len, aaa))

    li = [0,0,0]
    inds = li
    while sum(li)< ll:
        for i in range(3):
            b = map(lambda x: min_pos(aaa[i],x),inds)
            for j in range(len(b)):
                
            if inds[i] == len(aaa[i]):
                if j in range(3):
                    if j == j:
                        continue

#
# [e,i] =min(a)

# что сейчас произошло, мне потребовалась такая фунция от языка python
# которая с трудом реализуется исходя из тех парадигм, которые
# python реализует

#
# index of min of core
#
