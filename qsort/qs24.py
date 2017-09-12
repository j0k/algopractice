import random

def qsort(a):
    if len(a) <= 1:
        return a

    p = random.randint(0, len(a)-1)
    ep = a[p]

    c = [[], []]
    for i in range(len(a)):
        # range(len) is very useful constuction
        # aml: # - range(len )
        if i != p:
            e          =  a[i]
            c [ ep<e ] +=  [e]

            # aml
            # Local Comparison BreakOut Table Principle
            # e<ep  :: -> 0
            # e>=ep :: -> 1

    return qsort(c[0]) + [ep] + qsort(c[1])

def randperm(a):
    for i in range(len(a)):
        p = random.randint(0, len(a) - 1)
        a[i], a[p] = a[p], a[i]

    return a

A = randperm(range(20))

print A
print qsort(A)
