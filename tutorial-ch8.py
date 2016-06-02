# coding: UTF-8
# http://docs.python.jp/2.7/tutorial/errors.html
# 8. エラーと例外
from print_and_exec import *



print_and_exec(ur'''
"■8.1. 構文エラー"
while True print 'Hello world'
''')



print_and_exec(ur'''
"■8.2. 例外"
try_exec("10 * (1/0)")
print

try_exec("4 + spam*3")
print

try_exec("2' + 2")
''')



print_and_exec(ur'''
"■8.3. 例外を処理する - 1"
while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print "Oops!  That was no valid number.  Try again..."
''')



print_and_exec(ur'''
"■8.3. 例外を処理する - 2"
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
else: # executed when no exception catched
    f.close()
    print "i = {0}".format(i)
''')



print_and_exec(ur'''
"■8.3. 例外を処理する - 3(実行できるように修正)"
#for arg in sys.argv[1:]:
for arg in ["workfile.txt", "not_exist.txt"]:
    try:
        f = open(arg, 'r')
    except IOError:
        print 'cannot open', arg
    else:
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()
''')



print_and_exec(ur'''
"■8.3. 例外を処理する - 4"
try:
   raise Exception('spam', 'eggs')
except Exception as inst:
   print type(inst)     # the exception instance
   print inst.args      # arguments stored in .args
   print inst           # __str__ allows args to be printed directly
   x, y = inst.args
   print 'x =', x
   print 'y =', y
''')



print_and_exec(ur'''
"■8.3. 例外を処理する - 5"
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as detail:
    print 'Handling run-time error:', detail
''')



print_and_exec(ur'''
"■8.4. 例外を送出する - 1"
raise NameError('HiThere')
''')



print_and_exec(ur'''
"■8.4. 例外を送出する - 2"
try:
    raise NameError('HiThere')
except NameError:
    print 'An exception flew by!'
    raise
''')



print_and_exec(ur'''
"■8.4. 例外を送出する - "
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print 'My exception occurred, value:', e.value
''')



print_and_exec(ur'''
"■8.5. ユーザー定義例外 - 1"
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print 'My exception occurred, value:', e.value

raise MyError('oops!')
''')



print_and_exec(ur'''
"■8.5. ユーザー定義例外 - 2"
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        prev -- state at beginning of transition
        next -- attempted new state
        msg  -- explanation of why the specific transition is not allowed
    """

    def __init__(self, prev, next, msg):
        self.prev = prev
        self.next = next
        self.msg = msg
''')



print_and_exec(ur'''
"■8.6. クリーンアップ動作を定義する - 1"
try:
    raise KeyboardInterrupt
finally:
    print 'Goodbye, world!'
''')



print_and_exec(ur'''
"■8.6. クリーンアップ動作を定義する - 2"
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print "division by zero!"
    else:
        print "result is", result
    finally:
        print "executing finally clause"

divide(2, 1)
print

divide(2, 0)
print

divide("2", "1")
''')



print_and_exec(ur'''
"■8.7. 定義済みクリーンアップ処理"
with open("myfile.txt") as f:
    for line in f:
        print line,
''')

