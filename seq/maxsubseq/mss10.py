# 20.02.2018 in spagatin at 151 09:27
# 09:32 end

import random



def maxi(a,i,b,j):
    return (a,i) if a>=b else (b,j)

def mini(a,i,b,j):
    return (a,i) if a<=b else (b,j)


def maxseq(a):
    if len(a)<=1:
        return 0

    m,M,mi,Mi,le = a[0], a[0], 0, 0, a[0]
    t = 1
    A = []
    for i,e in enumerate(a):
        if e == le:
            continue
        elif (e>le and t > 0) or (e < le and t < 0):
            m,mi = mini(e,i,m,mi)
            M,Mi = maxi(e,i,M,Mi)
        else:
            A   += [(M-m,m,mi,M,Mi)]
            m,mi = mini(e,i,le,i-1)
            M,Mi = maxi(e,i,le,i-1)
            t    = t * -1
        le = e

    A += [(M-m,m,mi,M,Mi)]

    d_A   = list(map(lambda x:x[0], A))
    i_max = d_A.index(max(d_A))

    (d,m,mi,M,Mi) = A[i_max]
    l,r = min(mi,Mi), max(mi,Mi) # AML min,max /@ (mi,Mi)

    return (a[l:r+1], d, m,M, mi, Mi)

A = list(range(27))
A = random.sample(A, len(A))

print(A)
print(maxseq(A))


# indexing must be auto

# max_i ~ max <: e, i | i = e_i
# т.е. max_i похожа на max, но возвращает два значения e, i

# Q: верно ли что max возвращает e?
# A: yes

# Q: e_i это индекс элемента e в множестве его содержащем?
# A: да.

## вообще 'множество его содержащее'' это что-то что хорошо бы иметь возможность
## определить точно

# experession1 содержащее e
# должен имется способ, чтобы модифицировать e и использующие e конструкции

###
# f1 is use e
# f1 is return ret_e
# f2 ~ f1: ret_e -> ret_e ^ 2

# делаем функцию f2 такую, что она возводит ^2 вывод

# max: is return e
# max: have argv a
# max: e is an element of a
# max_i ~ max: e -> (e, index of e in a)

# впринципе можно было бы ограничиться пока этим
# т.е. чтобы на AML можно было написать подобные max_i, min_i функции

# но хочется более прикольную цель
