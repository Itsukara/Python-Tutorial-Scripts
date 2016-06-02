# coding: UTF-8
# http://docs.python.jp/2.7/tutorial/datastructures.html
# 5. データ構造
from print_and_exec import *


print_and_exec(ur'''
"■5.1. リスト型についてもう少し - 1"
"""
リストデータ型には、他にもいくつかメソッドがあります。リストオブジェクトのすべてのメソッドを以下に示します:

list.append(x)
   リストの末尾に要素を一つ追加します。 a[len(a):] = [x] と等価です。

list.extend(L)
   指定したリスト中のすべての要素を対象のリストに追加し、リストを拡張します。 a[len(a):] = L と等価です。

list.insert(i, x)
   指定した位置に要素を挿入します。第 1 引数は、リストのインデクスで、そのインデクスを持つ要素の直前に挿入が行われます。従って、 a.insert(0, x) はリストの先頭に挿入を行います。また a.insert(len(a), x) は a.append(x) と等価です。

list.remove(x)
   リスト中で、値 x を持つ最初の要素を削除します。該当する項目がなければエラーとなります。

list.pop([i])
   リスト中の指定された位置にある要素をリストから削除して、その要素を返します。インデクスが指定されなければ、 a.pop() はリストの末尾の要素を削除して返します。この場合も要素は削除されます。 (メソッドの用法 (signature) で i の両側にある角括弧は、この引数がオプションであることを表しているだけなので、角括弧を入力する必要はありません。この表記法は Python Library Reference の中で頻繁に見ることになるでしょう。)

list.index(x)
   リスト中で、値 x を持つ最初の要素のインデクスを返します。該当する項目がなければエラーとなります。

list.count(x)
   リストでの x の出現回数を返します。

list.sort(cmp=None, key=None, reverse=False)
   リストの項目を、インプレース演算 (in place、元のデータを演算結果で置き換えるやりかた) でソートします。引数はソート方法のカスタマイズに使えます。 sorted() の説明を参照してください。

list.reverse()
   リストの要素を、インプレース演算で逆順にします。

以下にリストのメソッドをほぼ全て使った例を示します:
"""

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
# a.push(555) # Error pushは無い
a.extend(b)
print a

"""
insert, remove, sort などのリストを操作するメソッドの戻り値はNone。
これは Python の変更可能なデータ構造全てについての設計上の原則。
"""
''')



print_and_exec(ur'''
"■5.1.1. リストをスタックとして使う"
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print stack
print stack.pop()
print stack
print stack.pop()
print stack.pop()
print stack
''')



print_and_exec(ur'''
"■5.1.2. リストをキューとして使う"
"本ファイルでは例を拡充しています"
from collections import deque

queue = deque(["Eric", "John", "Michael"])
print queue
queue.appendleft("Jim")
print queue
queue.append("Terry")
print queue

b = [2001, 2018]
c = [3, 6]
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
"■5.1.3. 関数型プログラミング用ツール - 1"
def f(x): return x % 3 == 0 or x % 5 == 0

print filter(f, range(2, 25))
''')



print_and_exec(ur'''
"■5.1.3. 関数型プログラミング用ツール - 2"
def cube(x): return x*x*x

print map(cube, range(1, 11))
''')



print_and_exec(ur'''
"■5.1.3. 関数型プログラミング用ツール - 3"
seq = range(8)
def add(x, y): return x+y

print map(add, seq, seq)

# 例を追加
triplet = zip(range(1,5), range(5,9), range(10,14))
print triplet

def muln(a):
  r = 1
  for x in a:
    r *= x
  return r

print map(muln, triplet)
''')



print_and_exec(ur'''
"■5.1.3. 関数型プログラミング用ツール - 4"
def add(x,y): return x+y

print reduce(add, range(1, 11))
print reduce(add, range(1, 11), 1000)
''')



print_and_exec(ur'''
"■5.1.3. 関数型プログラミング用ツール - 5"
def sum(seq):
    def add(x,y): return x+y
    return reduce(add, seq, 0)

print sum(range(1, 11))
print sum([])
''')



print_and_exec(ur'''
"■5.1.4. リストの内包表記 - 1"
squares = []
for x in range(10):
    squares.append(x**2)

print squares

squares = [x**2 for x in range(10)]
print squares
''')



print_and_exec(ur'''
"■5.1.4. リストの内包表記 - 2"
print [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print combs
''')



print_and_exec(ur'''
"■5.1.4. リストの内包表記 - 3"
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print [x*2 for x in vec]

# filter the list to exclude negative numbers
print [x for x in vec if x >= 0]

# apply a function to all the elements
print [abs(x) for x in vec]

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print [weapon.strip() for weapon in freshfruit]

# create a list of 2-tuples like (number, square)
print [(x, x**2) for x in range(6)]

# the tuple must be parenthesized, otherwise an error is raised
try_exec("[x, x**2 for x in range(6)]")

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print [num for elem in vec for num in elem]
''')



print_and_exec(ur'''
"■5.1.4. リストの内包表記 - 4"
 from math import pi
print [str(round(pi, i)) for i in range(1, 6)]
''')



print_and_exec(ur'''
"■5.1.4.1. ネストしたリストの内包表記 - 1"
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 11, 12],
]

print [[row[i] for row in matrix] for i in range(3)] # transpose
''')



print_and_exec(ur'''
"■5.1.4.1. ネストしたリストの内包表記 - 2"
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print transposed
''')


print_and_exec(ur'''
"■5.1.4.1. ネストしたリストの内包表記 - 3"
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print transposed
''')


print_and_exec(ur'''
"■5.1.4.1. ネストしたリストの内包表記 - 4"
print zip(*matrix)
''')


print_and_exec(ur'''
"■5.2. del 文"
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print a

del a[2:4]
print a

del a[:]
print a

del a
try_exec("print matrix") # Error (not defined)
''')



print_and_exec(ur'''
"■寄り道"
a=[]
a[:]="Abracadabra"
print a

a = list("Abracadabra")
print a
''')


print_and_exec(ur'''
"■5.3. タプルとシーケンス - 1"
t = 12345, 54321, 'hello!'
print t[0]

print t

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print u

# Tuples are immutable:
try_exec("t[0] = 88888") # Error

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print v
''')



print_and_exec(ur'''
"■5.3. タプルとシーケンス - 2"
empty = ()
singleton = 'hello', # <-- note trailing comma
print len(empty)
print len(singleton)
print singleton      # ('hello',) tupleであることを示すため「,」が付いてる？
''')


print_and_exec(ur'''
"■5.3. タプルとシーケンス - 3"
x, y, z = (1, 2, 3)
print x, y, z

(x, y, z) = "abc"
print x, y, z
''')



print_and_exec(ur'''
"■5.4. 集合型
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)               # create a set without duplicates
print fruit
print 'orange' in fruit                 # fast membership testing
print 'crabgrass' in fruit

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print a
print b
print a - b
print a | b
print a & b
print a ^ b
print

a = {x for x in 'abracadabra' if x not in 'abc'}
print a
''')



print_and_exec(ur'''
"■5.5. 辞書 - 1"
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
''')



print_and_exec(ur'''
"■5.5. 辞書 - 2"
print dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print {x: x**2 for x in (2, 4, 6)}
print dict(sape=4139, guido=4127, jack=4098)
''')



print_and_exec(ur'''
"■5.6. ループのテクニック - 1"
for i, v in enumerate('ABC'):
  print i, ':', v
''')

print_and_exec(ur'''
"■5.6. ループのテクニック - 2"
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print 'What is your {0}?  It is {1}.'.format(q, a)
''')


print_and_exec(ur'''
"■5.6. ループのテクニック - 3"
for i in reversed(range(1, 10, 2)):
  print i,
''')


print_and_exec(ur'''
"■5.6. ループのテクニック - 4"
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(set(basket)):
  print i
''')


print_and_exec(ur'''
"■5.6. ループのテクニック - 5"
knights = {'gallahad':'the pure', 'robin':'the brave'}
for k, v in knights.iteritems():
  print k, ':', v
''')



print_and_exec(ur'''
"■5.6. ループのテクニック - 6"
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print filtered_data
''')



print_and_exec(ur'''
"■5.7. 条件についてもう少し"
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print non_null

# 追加
n = 0
def nn(): global n; n += 1; return n
print nn() or  nn() or  nn() # 1
print nn() and nn() and nn() # 4
''')



print_and_exec(ur'''
"■寄り道 リストの比較"
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print a, b, c
print a == b # True
print a == c # True
print a is b # True
print a is c # False
print

a = (10, 20, 30)
b = a
c = (10, 20, 30)
print a, b, c
print a == b # True
print a == c # True
print a is b # True
print a is c # False
''')



print_and_exec(ur'''
"■5.8. シーケンスとその他の型の比較"
"followings are all True"
print (1, 2, 3)              < (1, 2, 4)
print [1, 2, 3]              < [1, 2, 4]
print 'ABC' < 'C' < 'Pascal' < 'Python'
print (1, 2, 3, 4)           < (1, 2, 4)
print (1, 2)                 < (1, 2, -1)
print (1, 2, 3)             == (1.0, 2.0, 3.0)
print (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
print (1, 2, 3)              < ("1", "2", "3") # number < string
''')

