# coding: UTF-8
# http://docs.python.jp/2.7/tutorial/introduction.html
# 形式ばらない Python の紹介
from print_and_exec import *



print_and_exec(ur'''
"■出力のフォーマット"
class Complex(object):
  _imagstr = "i" # class変数、先頭に"_"を付けprivate扱いと表示
  _seqnum  = 0   # class変数、先頭に"_"を付けprivate扱いと表示
  def __init__(self, realpart, imagpart):
    self._r = realpart
    self._i = imagpart
    self._id = Complex._seqnum
    Complex._seqnum += 1

class Human(object):
  def __init__(self, name, age):
    self._name = name
    self._age  = age

c = Complex(1.0, -1.0)
h = Human("Tom", 25)

import repr
print repr.repr(set('supercalifragilisticexpialidocious'))
print repr.repr(c) # ハッシュコードが印字されるだけ
print repr.repr(h) # ハッシュコードが印字されるだけ
print

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
     'yellow'], 'blue']]]
pprint.pprint(t, width=30)
pprint.pprint(c, width=70) # ハッシュコードが印字されるだけ
pprint.pprint(h, width=70) # ハッシュコードが印字されるだけ
print

import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print textwrap.fill(doc, width=40)
print

from string import Template
t = Template('${village}folk send $$10 to $cause.')
print t.substitute(village='Nottingham', cause='the ditch fund')

''')




print_and_exec(ur'''
"■ログ記録"
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
"""
デフォルトでは、info() と debug() による出力は抑制され、
出力は標準エラーに送信されます。
"""
''')



print_and_exec(ur'''
"■リスト操作のためのツール"
from array import array
a = array('H', [4000, 10, 700, 22222])
print a
print sum(a)
print a[1:3]
print

from collections import deque
d = deque(["task1", "task2", "task3"])
print d
d.append("task4")
print "Handling", d.popleft()
print d
print

import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print scores
print

from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange the list into heap order
heappush(data, -5)                 # add a new entry
print [heappop(data) for i in range(3)]  # fetch the three smallest entries
print

from decimal import *
x = Decimal('0.70') * Decimal('1.05')
print x
print x.quantize(Decimal('0.01'))  # round to nearest cent
print round(.70 * 1.05, 2)  

print Decimal('1.00') % Decimal('.10')
print 1.00 % 0.10
print sum([Decimal('0.1')]*10) == Decimal('1.0')
print sum([0.1]*10) == 1.0


getcontext().prec = 36
print Decimal(1) / Decimal(7)
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')



nprint_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')
