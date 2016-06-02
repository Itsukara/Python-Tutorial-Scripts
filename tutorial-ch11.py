# coding: UTF-8
# http://docs.python.jp/2.7/tutorial/stdlib2.html
# 11. 標準ライブラリミニツアー – その 2
from print_and_exec import *



print_and_exec(ur'''
"■11.1. 出力のフォーマット - 1"
import repr
print repr.repr(set('supercalifragilisticexpialidocious'))
''')



print_and_exec(ur'''
"■11.1. 出力のフォーマット - 2"
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]

print pprint.pprint(t, width=30)
''')



print_and_exec(ur'''
"■11.1. 出力のフォーマット - 3"
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print textwrap.fill(doc, width=40)
''')



print_and_exec(ur'''
"■11.1. 出力のフォーマット - 4"
import locale
print locale.setlocale(locale.LC_ALL, 'English_United States.1252')

conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.8
print locale.format("%d", x, grouping=True)

print locale.format_string("%s%.*f", (conv['currency_symbol'],
                           conv['frac_digits'], x), grouping=True)

#clean up
locale.setlocale(locale.LC_ALL, '')
''')



print_and_exec(ur'''
"■11.2. 文字列テンプレート - 1"
from string import Template
t = Template('${village}folk send $$10 to $cause.')
print t.substitute(village='Nottingham', cause='the ditch fund')
''')



print_and_exec(ur'''
"■11.2. 文字列テンプレート - 2"
t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
#print t.substitute(d) # エラーから回復できないためコメントアウト
print t.safe_substitute(d)
''')


print_and_exec(ur'''
"■11.2. 文字列テンプレート - 3"
import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'
print "example of following input: Ashley_%n%f, Ashley_%d#%n%f"
fmt = raw_input('Enter rename style (%d-date %n-seqnum %f-format):  ')

t = BatchRename(fmt)
date = time.strftime('%Y-%m-%d')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print '{0} --> {1}'.format(filename, newname)
''')



print_and_exec(ur'''
"■11.3. バイナリデータレコードの操作"
import struct

data = open('myfile.zip', 'rb').read()
start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print filename, hex(crc32), comp_size, uncomp_size

    start += extra_size + comp_size     # skip to the next header
''')



print_and_exec(ur'''
"■11.4. マルチスレッド"
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print 'Finished background zip of: ', self.infile

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print 'The main program continues to run in foreground.'

background.join()    # Wait for the background task to finish
print 'Main program waited until background was done.'
''')



print_and_exec(ur'''
"■11.1. 出力の11.5. ログ記録"
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
"■11.6. 弱参照"
import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
print d['primary']          # fetch the object if it is still alive

del a                       # remove the one reference
print gc.collect()          # run garbage collection right away

print d['primary']          # entry was automatically removed
''')


print_and_exec(ur'''
"■11.7. リスト操作のためのツール - 1"
from array import array
a = array('H', [4000, 10, 700, 22222])
print sum(a)

print a[1:3]
''')



print_and_exec(ur'''
"■11.7. リスト操作のためのツール - 2"
from collections import deque
d = deque(["task1", "task2", "task3"])
print d
d.append("task4")
print "Handling", d.popleft()
print d
''')



print_and_exec(ur'''
"■11.7. リスト操作のためのツール - 3"
unsearched = deque([""])
def breadth_first_search(unsearched):
    while len(unsearched) != 0:
      node = unsearched.popleft()
      for m in gen_moves(node):
          if is_goal(m):
              return m
          unsearched.append(m)
    return ""

def gen_moves(node):
  return [node+"0", node+"1"]

def is_goal(g):
  return g.count("001") + g.count("010") == 4
  
print breadth_first_search(unsearched)
''')



print_and_exec(ur'''
"■11.7. リスト操作のためのツール - 4"
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print scores
''')



print_and_exec(ur'''
"■11.7. リスト操作のためのツール - 5"
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange the list into heap order
heappush(data, -5)                 # add a new entry
print [heappop(data) for i in range(3)]  # fetch the three smallest entries
''')



print_and_exec(ur'''
"■1.8. 10 進浮動小数演算 - 1"
from decimal import *
x = Decimal('0.70') * Decimal('1.05')
print x
print x.quantize(Decimal('0.01'))  # round to nearest cent
print round(.70 * 1.05, 2)  

''')



print_and_exec(ur'''
"■1.8. 10 進浮動小数演算 - 2"
print Decimal('1.00') % Decimal('.10')
print 1.00 % 0.10
print sum([Decimal('0.1')]*10) == Decimal('1.0')
print sum([0.1]*10) == 1.0
''')



print_and_exec(ur'''
"■1.8. 10 進浮動小数演算 - 3"
getcontext().prec = 36
print Decimal(1) / Decimal(7)
''')
