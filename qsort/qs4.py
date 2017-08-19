# 21.06.2017

import random

A = [1,10,2,3,4,-5,20,1,1,43,20]

def qsort(a):
    l = len(a)
    b = a + [None for i in range(l)]

    go = True
    bounds_in = [[0,len(a)]]
    bounds_out = [[0,len(b)]]
    while len(bounds_in)>0:
        left_b = bounds_in[0][0]
        right_b =bounds_in[0][1]

        ll = right_b - left_b

        mid_l = bounds_out[0][0]
        mid_r = int ( (bounds_out[0][1] - bounds_out[0][0])/2 )
        p = left_b + int(random.random() * ll)
        pb = b[p]

        del bounds_in[0]
        # p_out_i_l = m
        for i in range(ll):
            pi = left_b + i
            if b[pi] == None:
                continue
            elif b[pi] <= pb:
                c = b[pi]
                b[pi] = None
                b[mid_l] = c

                mid_l += 1
            else:
                c = b[pi]
                b[pi] = None
                b[mid_r] = c

                mid_r += 1

        if mid_l > bounds_out[0][0]:
            bounds_in.append([bounds_out[0][0], mid_l])
        #if mid_r > int ( (bounds_out[0][1] - bounds_out[0][0])/2 ):
        #    bounds_in.append([bounds_out[0][0], mid_l])

        # qsort(left), pa, qsort(right)

        i = 0
        j = 0
        while i < (len(b)):
            j += 1
            if b[i] == None:
                del b[i]
                b.append(None)
            else:
                i += 1
            if j == len(b):
                break;

    return b

print qsort(A)

# don't work. I just think about non-recursive qsort version
