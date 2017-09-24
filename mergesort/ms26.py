import random


def m(a,b):
    i,j = 0,0
    c = []

    while i+j < len(a) + len(b):
        if i == len(a):
            c += [b[j]]
            j += 1
        elif j == len(b):
            c += [a[i]]
            i += 1
        elif a[i] <= b[j]:
            c += [a[i]]
            i += 1
        else:
            c += [b[j]]
            j += 1

    return c

def ms(a):
    p = int(len(a)/2)

    if p == 0:
        return a

    return m(ms(a[:p]),ms(a[p:]))

def randperm(a):
    return random.sample(a,len(a))


A = randperm(range(20))

print A
print ms(A)


# AML details:
#
# here we want to bypass the bound conditions
# a[i], b[j]
# merge(a,b):
#   i in a.inds & j in b.inds:
#     a[i] <= b[j] ==> c += [a[i]] esle c += [b[j]]
#
# declarative paradigm with NLP associatiove purposes
#
# a[i], b[j]
# merge(a,b):
#   i in a.inds & j in b.inds || iterate by 1: // || iterate by step
#     a[i] <= b[j] ==> c += [a[i]] esle c += [b[j]]
#
# merge(a,b):
#   i in a.inds & j in b.inds || iterate together (i,j) by 1 : // || iterate by step
#     a[i] <= b[j] ==> c += [a[i]] esle c += [b[j]]
#
# Quessed Interpretation Paradigm
#
# merge(a,b):
#   i in a.inds: // for by quess
#     j in b.inds || iterate together (i,j) by 1 : // || iterate by step
#       a[i] <= b[j] ==> c += [a[i]] esle c += [b[j]]
#
#
# SO in AML we have stable AML and flexible AML with quessing and associative sences
