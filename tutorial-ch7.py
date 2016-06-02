# coding: UTF-8
# http://docs.python.jp/2.7/tutorial/inputoutput.html
# 7. 入力と出力
from print_and_exec import *



print_and_exec(ur'''
"■7.1. ファンシーな出力の書式化 - 1"
s = 'Hello, world.'
print repr(str(s))
print repr(repr(s))
print repr(str(1.0/7.0))
print repr(repr(1.0/7.0))
print

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print s

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print hellos

# The argument to repr() may be any Python object:
print repr((x, y, ('spam', 'eggs')))
''')



print_and_exec(ur'''
"■7.1. ファンシーな出力の書式化 - 2"
for x in range(1, 11):
    print repr(x).rjust(2), repr(x*x).rjust(3),
    # Note trailing comma on previous line
    print repr(x*x*x).rjust(4)
print

for x in range(1,11):
    print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)
''')

print_and_exec(ur'''
"■7.1. ファンシーな出力の書式化 - 3(おまけ)"
for x in range(-1, 5):
  xx = x*x*x*100
  print '{0:*<+8} {1:x>-8,.1f} {2: ^8,d} {3:#010x}'.format(xx, xx, xx, xx)
''')



print_and_exec(ur'''
"■7.1. ファンシーな出力の書式化 - 4"
print '12'.zfill(5)
print '-3.14'.zfill(7)
print '3.14159265359'.zfill(5)
''')



print_and_exec(ur'''
"■7.1. ファンシーな出力の書式化 - 5"
print 'We are the {} who say "{}!"'.format('knights', 'Ni')
''')



print_and_exec(ur'''
"■7.1. ファンシーな出力の書式化 - 6"
print '{0} and {1}'.format('spam', 'egg')
print '{1} and {0}'.format('spam', 'egg')
''')



print_and_exec(ur'''
"■7.1. ファンシーな出力の書式化 - 7"
print 'This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible')
''')



print_and_exec(ur'''
"■7.1. ファンシーな出力の書式化 - 8"
print 'The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                    other='Georg')
''')



print_and_exec(ur'''
"■7.1. ファンシーな出力の書式化 - 9"
import math
print 'The value of PI is approximately {}'.format(math.pi)
print 'The value of PI is approximately {!r}'.format(math.pi)
print 'The value of PI is approximately {!s}'.format(math.pi)
print 'The value of PI is approximately {0:.3f}'.format(math.pi)
''')


print_and_exec(ur'''
"■7.1. ファンシーな出力の書式化 - 10"
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print '{0:10} ==> {1:10d}'.format(name, phone)
''')


print_and_exec(ur'''
"■7.1. ファンシーな出力の書式化 - 11"
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print ('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
       'Dcab: {0[Dcab]:d}'.format(table))
''')


print_and_exec(ur'''
"■7.1. ファンシーな出力の書式化 - 12"
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)
''')



print_and_exec(ur'''
"■7.2. ファイルを読み書きする"
# mode can be 'r'   'w'   'a'   'r+'  : text
#             'rb'  'wb'  'ab'  'r+b' : binary 
f = open('workfile.txt', 'r')
print f
''')



print_and_exec(ur'''
"■7.2.1. ファイルオブジェクトのメソッド - 1"
print repr(f.read()) # read all characters as a string
print repr(f.read())
f.close()
''')



print_and_exec(ur'''
"■7.2.1. ファイルオブジェクトのメソッド - 2"
f = open('workfile.txt', 'r')
print repr(f.readline())
print repr(f.readline())
f.close()
''')


print_and_exec(ur'''
"■7.2.1. ファイルオブジェクトのメソッド - 3"
f = open('workfile.txt', 'r')
for line in f:
    print line,
f.close()
''')



print_and_exec(ur'''
"■7.2.1. ファイルオブジェクトのメソッド - 4"
f = open('workfile2.txt', 'w')
f.write("This is a test\n")

value = ('the answer', 42)
s = str(value)
f.write(s)
f.close()

import os
os.system("type workfile2.txt")
''')



print_and_exec(ur'''
"■7.2.1. ファイルオブジェクトのメソッド - 5"
f = open('workfile3.txt', 'r+')
f.write('0123456789abcdef')
f.seek(5)      # Go to the 6th byte in the file
print f.read(1)
f.seek(-3, 2)  # Go to the 3rd byte before the end
print f.tell() # Get postion in the file
print f.read(1)
''')



print_and_exec(ur'''
"■7.2.1. ファイルオブジェクトのメソッド - 6"
f.close()
f.read()
''')



print_and_exec(ur'''
"■7.2.1. ファイルオブジェクトのメソッド - 7"
with open('workfile.txt', 'r') as f:
    read_data = f.read()
print f.closed
''')



print_and_exec(ur'''
"■7.2.2. json による構造化されたデータの保存 - 1 (加筆)"
import json
data = (1.23, 'test', [c for c in 'abcde\n'], 
        {'x':5.0, 'y':7}, u"日本語はOK?")
print repr(data)
print

jsondata = json.dumps(data) # convert to json
print repr(jsondata)
print

x = json.loads(jsondata)    # convert from json
print repr(x)
''')



print_and_exec(ur'''
"■7.2.2. json による構造化されたデータの保存 - 2 (加筆)"
with open("data.json", "w") as f:
  json.dump(data, f)
with open("data.json", "r") as f:
  x = json.load(f)
  print repr(x)

"(注) JSONではクラスオブジェクトをシリアライズできない"
''')



print_and_exec(ur'''
"■7.2.x. pickle による構造化されたデータの保存 - 1 (加筆)"
"PickleはPythonの独自形式だが、任意のPythonオブジェクトをシリアライズ可能"
import pickle
data = (1.23, 'test', [c for c in 'abcde\n'], 
        {'x':5.0, 'y':7}, u"日本語はOK?")
print data
print

pickledata = pickle.dumps(data)
print repr(pickledata)
print

x = pickle.loads(pickledata)
print repr(x)
''')


print_and_exec(ur'''
"■7.2.x. pickle による構造化されたデータの保存 - 2 (加筆)"
with open("data.pickle", "w") as f:
  pickle.dump(data, f)

with open("data.pickle", "r") as f:
  x = pickle.load(f)
  print x
''')
