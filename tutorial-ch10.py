# coding: UTF-8
# http://docs.python.jp/2.7/tutorial/stdlib.html
# 10. 標準ライブラリミニツアー
from print_and_exec import *



nprint_and_exec(ur'''
"■10.1. OSへのインタフェース -1"
import os
print os.getcwd()

os.system('mkdir today')
print os.chdir('today')
''')



nprint_and_exec(ur'''
"■10.1. OSへのインタフェース -2"
import os
print dir(os)

help(os)
''')



nprint_and_exec(ur'''
"■10.1. OSへのインタフェース -3"
import shutil

shutil.copyfile(r'..\data.db', 'archive.db')
shutil.move('archive.db', 'move.db')

os.system('dir move.db')

# cleanup
os.system('del move.db')
os.chdir("..")
os.system('rmdir today')
''')



print_and_exec(ur'''
"■10.2. ファイルのワイルドカード表記"
import glob
print glob.glob("*.py")
''')



print_and_exec(ur'''
"■10.3. コマンドライン引数"
import sys
print sys.argv
''')



print_and_exec(ur'''
"■10.4. エラー出力のリダイレクトとプログラムの終了"
sys.stderr.write('Warning, log file not found starting a new one\n')
''')



print_and_exec(ur'''
"■0.5. 文字列のパターンマッチング"
import re
print re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print 'tea for too'.replace('too', 'two')
''')



print_and_exec(ur'''
"■10.6. 数学 - 1"
import math
print math.cos(math.pi / 4.0)
print math.log(1024, 2)

''')



print_and_exec(ur'''
"■10.6. 数学 - 2"
import random
print random.choice(['apple', 'pear', 'banana'])
print random.sample(xrange(100), 10)   # sampling without replacement
print random.random()                  # random float
print random.randrange(6)              # random integer chosen from range(6)
''')



nprint_and_exec(ur'''
"■10.7. インターネットへのアクセス"
import urllib2
for line in urllib2.urlopen('https://httpd.apache.org/docs/2.4/new_features_2_4.html'):
  if '2.4.' in line :
    print line

# ERROR
#import smtplib
#server = smtplib.SMTP('localhost')
#server.sendmail('iitt21-all@yahoo.co.jp', 'iitt21-all@yahoo.co.jp',
#"""To: anonymous@yahoo.co.jp
#From: nobody@yahoo.co.jp
#
#Beware the Ides of March.
#""")
#server.quit()
''')



print_and_exec(ur'''
"■10.8. 日付と時刻"
from datetime import date
now = date.today()
print now
print now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

# dates support calendar arithmetic
birthday = date(1961, 2, 5)
age = now - birthday
print age.days
''')



print_and_exec(ur'''
"■10.9. データ圧縮"
import zlib
s = 'witch which has which witches wrist watch'
print len(s)
t = zlib.compress(s)
print len(t)

print zlib.decompress(t)
print "crc32={:08x}".format(zlib.crc32(s))
''')



print_and_exec(u'''
"■10.10. パフォーマンスの計測"
from timeit import Timer
print Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print Timer('a,b = b,a', 'a=1; b=2').timeit()
print

print Timer('sum([i*i for i in range(1, 10)])').timeit()
print Timer("""
sum = 0
for i in range(1, 10):
  sum += i*i
""").timeit()
''')



print_and_exec(u'''
"■10.11. 品質管理 - 1"
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print average([20, 30, 70])
    40.0
    """
    return sum(values, 0.0) / len(values)

import doctest
print doctest.testmod()   # automatically validate the embedded tests
''')



print_and_exec(u'''
"■10.11. 品質管理 - 2"
import os

os.system("type average.py")

os.system("python average.py")
''')

