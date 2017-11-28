# 22.11.2017 - end: 11:35, Old Hospital, Lima, Cyprus

import random

def qs(a):
    if len(a)<=1:
        return a

    p = len(a)/2
    lr = [[],[]]

    for i,e in enumerate(a):
        if not i == p:
            lr[not e <= a[p]] += [e]

    #for i,e in enumerate(a):
    #    i!=p, $R[#1, #2], e<a[p]=>#1 += [e] else #2 += [2]:


    lr = map(qs, lr)
    return lr[0] + [a[p]] + lr[1]

A = range(25)
A = random.sample(A, len(A))

print A
print qs(A)

# идея символа $R возрата локального блока это сильно!
# эта идея должна быть совмещена с автоматическим именование всех $R где ручками
# нужно


# NN idea: именование переменных
# как то автоматически на основе опенсорса; учить комп именовать переменные
# можно на примере github и проектов в нём

# вообще есть и другая задача - по коду понимать контекст и чём проект
