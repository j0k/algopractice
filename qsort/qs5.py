# 21.06.2017
A = [1,1,2,30,203,201,1,-10,2,3,45,7]

def qsort(a):
    if len(a) <= 1: # error - I checked it after [1,2,3] = ...
        return a

    [l,pi,p] = [len(a), int(len(a)/2), a[int(len(a)/2)] ]

    B = [[],[]]
    for i in range(l):
        if i == pi:
            continue
        e = a[i]
        B[ int(e>= p) ] += [e] # cool idea

    return qsort(B[0]) + [p] + qsort(B[1]) # error - i don't exec qsort

print qsort(A)

# cool idea to use if/switch as an index
# it would be usefull to advance that concept

# A [ f(x) ].append(g(f))
# case(f) will have an option to change behavior of wrapper fucnction []
# if error then no append

# f(x):
#   if x> 10:
#     1
#   elif x> 8:
#     2
#   elif x == 1
#     error

#
# it also be usefull to

# Connected Expressions Evaluation Paradigm
# that means
# if we executed something - for example f(x)
# practically in every moment we can call the f(x) result
# also after A [ case(x) ]. append(f(x))

# case(x) &repeated
# that means that we use case(x) as a func which don't change state
# case(x),case(x),case(x) = c,c,c not c1,c2,c3 where (ci != cj)

# expression paradigm will help to use result for example
#
# f(x):
#    if x['param']: return (x)
#    if x['w'] > 100000: return err(BIG_WEIGHT)
#

#
# for i in range(l):
#     if i == pi:
#         continue
#     e = a[i]
#     B[ int(e>= p) ] += [e] # cool idea
#
# for i in range(l):
#     if i == pi:
#         continue
#     B[(_ >= p)] += [_]) a[i]
#     B[ int(e>= p) ] += [e] # cool idea
#     # maybe
#     # another form is B[(_ >= p)] += [_]) a[i]
#     # another form B[].(>=p).+=.[] a[i]
#     # or # another form B[].(>=p).+=.[_] a[i]
