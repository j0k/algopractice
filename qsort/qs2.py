# 19.06.2017

A = [1,2,3,4,5,6,7,8,4,44,44,3,33,1,1,-1]

def qsort(a):
    return a if len(a)<= 1 else \
        qsort(filter( lambda x: x <= a[0], a[1:])) + \
         [a[0]] + \
        qsort(filter( lambda x: x >  a[0], a[1:]))

# myLang
# qsort(a): a if len(a)<= 1 else qsort( a( # <= a[0] ) ),a[0],qsort( a( # > a[0] ) )

# qsort(a):
# p = ?a
# a if len(a)<= 1 else qsort( a[^(p)] ( # <= a[p] ) ),[a[p]],qsort( a[^(p)]( # > a[p] ) )

# a if len(a)<= 1 else qsort( a[^p] ( # <= a[p] ) ),[a[p]],qsort( a[^p]( # > a[p] ) )

#  a if len(a)<= 1 else b=a[^p];qsort( b( # <= a[p] ) ),[a[p]],qsort( b( # > a[p] ) )

#  a if len(a)<= 1 else b=a[^p];self( b( # <= a[p] ) ),[a[p]],self( b( # > a[p] ) )

# qsort(a):
# (e,p) = ?a;
# b = a[^p];
# self( b( # <= a[p] ) ), [a[p]],self( b( # > a[p] ) )

# qsort(a):
# (_,p) = ?a;
# b = a[^p];
# (L,R) = b( # <= a[p] )
# self(l), [ a[p] ], self(R)

# optimal version
#
# qsort(a):
# ret a if ( #a <= 1 )
# (ap,p) = ?a;
# [L,R] = a[^p] ( (# <= ap),(# > ap) )
# self(l), ap, self(R)

# optimal version
#
# qsort(a):
# ret a if ( #a <= 1 ) else
#   (ap,p) = ?a;
#   [L,R] = a[^p] ( (# <= ap),(# > ap) )
#   self(l), ap, self(R)

# optimal version
#
# qsort(a):
# ret a if ( #a <= 1 ) else
#   (ap,p) = ?a;
#   [L,R] = a[^p] ( <= ap, > ap )
#   self(l), ap, self(R)

# optimal version
#
# qsort(a):
# ret a if ( #a <= 1 ) else
#   (ap,p) = ?a;
#   [L,R] = a[^p] ( <=, > ap )
#   self(l), ap, self(R)


# first compile
# run on data
# execution will detailez object types ( that a is array )
# recompile
# get superoptimized code

# _asm(qsort) -> get assemblers code
# _inter(qsort) -> get intermediate code

# optimal version
#
# [1]: qsort(a):
# [2]:   ret a if ( #a <= 1 ) else
# [3]:    (ap,p) = ?a;
# [4]:    [L,R] = a[^p] ( (# <= ap),(# > ap) )
# [5]:    self(l), ap, self(R)
#
# code = _inter(qsort)
# code[3]
# ccode = _ccode(qsort)
# ccode[3]
# lispcode = _lisp(qsort)
# code[3]
#
#
#

#
# abstract qsort(a):
#  a if ( #a == 0 ) else qsort(_1),[_2],qsort(_3)
#
# def qsort(a)
#   (ap,p) = ?a;
#   _2 = ap
#   [_1,_3] = a[^p] (<=,> ap)


# we can get that constuction using
# optimal version
#
# qsort(a):
# ret a if ( #a <= 1 ) else
#   (ap,p) = ?a;
#   [L,R] = a[^p] ( <=, > ap )
#   self(l), [ap], self(R)
#
# abstragate (qsort)
#
# mylang will have a very powerful abstragate method
# myLang - Abstract Juicy Collaborative Language (ajcl)


# you can do
# compform = _completeform(qsort)
# cf_qsort = compile(compform)
#
# print compform
# '''
# qsort(array a):
#   if #a <= 1:
#     return a
#   else:
#     (a_element, a_position) = random_choice (a)
#     # (ap, p) = random_choice (a) // i don't know how it will be better
#     a1 = a[out a_position]
#     [L,R] = b.[select(<=,> a_element)]
#     return qsort(L), [ap], qsort(R)
# '''
# a[^p] = a[ .. ^p ..] = a[ out(p) ] = a[ out p ] = a[]

#
# I don't show the most powerful interactive method for JACL
# maybe it will be J DIALOGED and C A L (JDCAL) or adl
#
# let try
#
# > def qsort(a)
#
# << created def qsort(a)
#
# > it will sort a
#
# << OK. _algorithm_sort in qsort.class
#
# > if #a <= 1 it will return a
#
# << OK. return a if #a <= 1
#
# > show
#
# << return a if #a <= 1
#
# > show object
#
# << def qsort(a)
#      return a if #a <= 1
#
# > it will take random element in a
#
# < OK. element = ?a
#
# > and take all elements which <= element and > element
#
# << [A,B] = b( <=, > element )
#
# let A be Left, B - right
#
# << [Left, right] = b(<=, > element)
#
# > element = elem
#
# << elem = ?a
# << [Left, right] = a(<=, > elem)
#
# > if #a >= 1 it will return left,[elem],right
#
# << if #a >= 1: return left,[elem],right
#
# > show all
#
# << def qsort(a)
#      return a if #a <= 1
#      elem = ?a
#      [Left, right] = a(<=, > elem)
#      if #a >= 1: return left,[elem],right
#
# > format it and show
#
# << def qsort(a)
#      return a if #a <= 1
#      elem = ?a
#      [Left, right] = a(<=, > elem)
#      return left,[elem],right if #a >= 1
#
# ** also I can click on qsort and write examples of input data a
# ** a = [1,2,3,4,2,1,0]
#
# ** when I write >> make release version it will ask type(a) ~ int[]?
# then I check that type(a) ~ double[] or real[] or float[] or just
# example a = [-1,10,-2.0]
#
# ** also I can run qsort on test dataset at each moment I want during the development
# ** also i can use unicode to code лев,прав = a(<=, > elem)

## ** I found the error - cause i don't need to remove all elements = ?a
#
# > i don't need to remove all elements == elem
#
# <<? look at: [Left, right] = a(<=, > elem)
#
# > I have to drop a[elem position] before selecting
#
# << elem,position = ?a
#    [Left, right] = a[^postion](<=, > elem)
#
# > format to short form and show all
#
# << def qsort(a)
#      a if #a <= 1 else:
#        elem, position = ?a
#        [Left, right] = a[^position](<=, > elem)
#        return left,[elem],right
#
# ** also at each moment I can choose any line and run to it.
#
# > qsort to lispform
#
# << (defun qsort(a)
#      (if (<= #a , 1),
#         a,
#        (= [elem, position],? a)
#        (= [Left, right], (<=, > elem) a[^position])
#        (, left, [elem] ,right)))
#
# *** it's all about smart parsers with feedback and backpropogation
#
# ** it will be usefull to have simple plugin|lib to write GUI desktop app,
# iOS apps, Android apps and others 

print qsort(A)
print qsort([-1,-2,-3])
