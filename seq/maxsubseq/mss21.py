import random

def maxseq(a):
    if len(a) <= 1:
        return 0

    m,M,el = a[0],a[0],a[0]
    t = True

    d = 0
    for (i,e) in enumerate(a):
        if not ((t and e>=el) or (not t and e=<el)):
            m, M = min(el,e), max(el,e)
            t = not t

        m, M = min(m,e), max(M,e)
        if d < M-m:
            d = M-m

        el = e
    return d

A = range(31)
A = random.sample(A, len(A))

print(A)
print(maxseq(A))

# AML natural operations


# before = s:'elem before `e in `a'
# for (e, el as before) in a:
#     order ~= e<el
#     if order changed:
#         m,M = min,max (el,e)
#         order = e<el

# we can start from this key words:
#  1. ~=
#  2. changed
#  3. before

# which connected to logic structure
# principle:
