# coding: UTF-8
# http://docs.python.jp/2.7/tutorial/introduction.html
# 形式ばらない Python の紹介
from print_and_exec import *



print_and_exec(ur'''
"■Handling Exceptions 1"
while True:
  try:
    x = int(raw_input("Input number: "))
    break
  except ValueError:
    print "Your input is not number. Try aggain"
''')




print_and_exec(ur'''
"■Handling Exceptions 2"
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    exit()
except ValueError:
    print "Could not convert data to an integer."
    exit()
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
else:
    f.close()
    print "i = {0}".format(i)
''')



print_and_exec(ur'''
"■Defining Clean-up Actions"
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print "division by zero!"
    except Exception as e: 
        print "Error:" + repr(e)
        exit()
    else:
        print "result is", result
    finally:
        print "executing finally clause"
divide(2, 1)
print
divide(2, 0)
print
divide("2", "1")
print
''')
