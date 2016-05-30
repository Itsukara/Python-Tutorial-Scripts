# coding: UTF-8
# http://docs.python.jp/2.7/tutorial/introduction.html
# 形式ばらない Python の紹介
from print_and_exec import *



print_and_exec(ur'''
"■Fancier Output Formatting"
s = 'Hello, world.\nGoodby, cosmos.'
print str(s)
print
print repr(s)
print
print str(1.0/7.0)
print repr(1.0/7.0)
print repr((s, (1, 2, 3)))
''')



print_and_exec(ur'''
"■repr.rjust, format"
for x in range(-1, 5):
  print repr(x).ljust(3), repr(x*x).rjust(4),
  print repr(x*x*x).center(5), repr(x).zfill(6)
print

for x in range(-1, 5):
  xx = x*x*x*100
  print '{0:*<+8} {1:x>-8,.1f} {2: ^8,d} {3:#010x}'.format(xx, xx, xx, xx)
print

print '{} and {}'.format('spam', 'egg')
print '{0} and {1}'.format('spam', 'egg')
print '{1} and {0}'.format('spam', 'egg')
print 'I like {0}, {food1} and {food2}'\
      .format('apple', food1='spam', food2='egg')
print

import math
print 'PI = {}'.format(math.pi)
print 'PI = {!s}'.format(math.pi)
print 'PI = {!r}'.format(math.pi)
print 'PI = {0:8.2f}'.format(math.pi)
print 'PI = %9.3f' % math.pi
print

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print ('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
       'Dcab: {0[Dcab]:d}'.format(table))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)
''')



print_and_exec(ur'''
"■Reading Files"
# mode can be 'r'  'w'  'a'  'r+'  'rb'  'wb'  'ab'  'r+b' 
f = open('workfile.txt', 'r')
print repr(f.readline())
print repr(f.readline())
f.close()
print

f = open('workfile.txt', 'r')
alldata = f.read() # read all characters
print len(alldata)
print repr(alldata[0:50])
f.close()
print

f = open('workfile.txt', 'r')
for line in f: # read one line
  print repr(line)
f.close()
print

with open('workfile.txt', 'r') as f:
  lines = f.readlines() # read all lines as list
  print lines
  # autoclosed
''')



print_and_exec(ur'''
"■Writing Files"
f = open('tempfile.txt', 'w')
f.write("This is a test\n")

a = [1, 3, 5]
f.write(str(a)+"\n")
print f.tell()

f.seek(5)     # seek to 5th byte in file
f.write("X")
f.seek(3, 1)  # seek 3 bytes forward
f.write("Y")
f.seek(-4, 2) # seek 4th byte before the end
f.write("Z")
f.close()
print

with open('tempfile.txt', 'r') as f:
  for line in f: # read one line
    print repr(line)
''')



print_and_exec(ur'''
"■Saving structured data with json"
import json
data = (1.23, 'test', [c for c in 'abcde\n'], 
        {'x':5.0, 'y':7}, u"日本語はOK?")
print repr(data)
print

jsondata = json.dumps(data)
print repr(jsondata)
print

x = json.loads(jsondata)
print repr(x)
print

with open("data.json", "w") as f:
  json.dump(data, f)
with open("data.json", "r") as f:
  x = json.load(f)
  print repr(x)

"(注) JSONではクラスオブジェクトをシリアライズできない"
''')



print_and_exec(ur'''
"■Pickle"
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
print

with open("data.pickle", "w") as f:
  pickle.dump(data, f)

with open("data.pickle", "r") as f:
  x = pickle.load(f)
  print x
''')
