# coding: UTF-8
# http://docs.python.jp/2.7/tutorial/introduction.html
# 形式ばらない Python の紹介
from print_and_exec import *



print_and_exec(ur'''
"■list - details"
a = [66.25, 333, 333, 1, 1234.5]
b = [2001, 2018]
print a
print a.count(333)
print a.index(333)
print

a.insert(2, 400)
print a
a.remove(333)
print a
a.reverse()
print a
a.sort()
print a
print

print a.pop()
print a
# a.push(555) # Error
a.extend(b)
print a
"""
insert, remove, sort などのリストを操作するメソッドの戻り値がNone。
これは Python の変更可能なデータ構造全てについての設計上の原則。
"""
''')



print_and_exec(ur'''
"■deque - suitable for append and pop from left"
b = [2001, 2018]
c = [3, 6]
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print queue
queue.appendleft("Jim")
print queue
queue.append("Terry")
print queue
queue.extendleft(b)
print queue
queue.extend(c)
print queue
print

print queue.popleft()
print queue
print queue.pop()
print queue
print

queue.rotate(2)
print queue
''')



print_and_exec(ur'''
"■list - functional programming - filter(), map(), reduce()"
def f(x): return x % 3 == 0 or x % 5 == 0
print filter(f, range(2, 25))
print

def cube(x): return x*x*x
print map(cube, range(1, 11))
print

seq1 = range(8)
seq2 = range(10, 18)
seq3 = range(100, 108)
def mul(x, y, z): return x*y*z
print map(mul, seq1, seq2, seq3)
print

def muln(a):
  r = 1
  for x in a:
    r *= x
  return r
triplet = zip(seq1, seq2, seq3)
print triplet
print map(muln, triplet)
print

def add(x, y): return x+y
print reduce(add, range(1, 11))
print reduce(add, range(1, 11), 1000)
print

def notb(x): return x != "b"
print filter(notb, "not but best buy")
print

def notb(x): return x != u"語"
print filter(notb, u"日本語でOK、英語もOK")
''')



print_and_exec(ur'''
"■List Comprehensions"
squares  = [x**2 for x in range(10)]
squares2 = map(lambda x: x**2, range(10))
print squares
print squares2
print

tuples1 = [(x, y, x+y) for x in [1,2,3] for y in [1,3,5] if x != y]
print tuples1
print

vec = [[1,2,3], [4,5,6], [7,8,9]]
print [n*n for e in vec for n in e] # flatten
''')



print_and_exec(ur'''
"■List Comprehensions 2"
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 11, 12],
]
print [[row[i] for row in matrix] for i in range(3)]
print zip(*matrix)
print

del matrix[1]
print matrix
del matrix
# print matrix # Error (not exist)
''')



print_and_exec(ur'''
"■Tuples and Sequences"
t = 123, 456, 'hello'
print t
t = t, [10, 20, 30]
print t
try_exec("t[1] = [1, 2, 3]") # Error (imutable)
t[1][0] = 1                  # value of element can be modified
print t
print

empty = ()
singleton = 'hello', # "," is meaningfull
print empty
print singleton
print

x, y, z = (1, 2, 3)
print x, y, z
(x, y, z) = "abc"
print x, y, z
''')



print_and_exec(ur'''
"■Sets"
t = 10, 20, 30
s = set(t)
print s
print 20.0 in s
print

a = set('abracadabra')
b = set('alacazam')
print a
print b
print a - b
print a | b
print a & b
print a ^ b
print

# set = {x for x in 'abracadabra' if x not in 'abc'} # shoud not overwrite python keyword
s = {x for x in 'abracadabra' if x not in 'abc'}
print s
''')



print_and_exec(ur'''
"■Dictionaries"
tel = {'jack': 4098, 'sape': 4139}
print tel
print

tel['guido'] = 4127 # add entry
print tel
print tel['jack']   # get value
print

del tel['sape']
print tel
print

print tel.keys()
print 'guido' in tel
print

print dict([('a', 10), ('b', 20), ('c', 30)])
print {name: age for name in 'ABC' for age in (21, 22, 23)}
''')



print_and_exec(ur'''
"■Looping Techniques"
for i, v in enumerate('ABC'):
  print i, ':', v
print

for n, a in zip('ABC', (31, 32, 33)):
  print n, ':', a
print

for i in reversed(range(1, 10, 2)):
  print i,
print
print

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(set(basket)):
  print i
print

knights = {'gallahad':'the pure', 'robin':'the brave'}
for k, v in knights.iteritems():
  print k, ':', v
print

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print filtered_data
''')



print_and_exec(ur'''
"■More on Conditions"
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print a, b, c
print a == b
print a == c
print a is b
print a is c
print

# imutables can't be same
a = (10, 20, 30)
b = (10, 20, 30)
print a is b
print

# and/or short circuite
n = 0
def nn(): global n; n += 1; return n
print nn() or  nn() or  nn()
print nn() and nn() and nn()
''')



print_and_exec(ur'''
"■Comparing Sequences and Other Types"
print (1, 2, 3)              < (1, 2, 4)
print [1, 2, 3]              < [1, 2, 4]
print 'ABC' < 'C' < 'Pascal' < 'Python'
print (1, 2, 3, 4)           < (1, 2, 4)
print (1, 2)                 < (1, 2, -1)
print (1, 2, 3)             == (1.0, 2.0, 3.0)
print (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
print (1, 2, 3)              < ("1", "2", "3")
''')

