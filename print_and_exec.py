# coding: UTF-8
# http://docs.python.jp/2.7/tutorial/introduction.html
# 形式ばらない Python の紹介

def try_exec(script):
  try:
    exec script in globals() # globals()を付けないとch9は動かない
  except Exception as e: 
    print "Error:" + repr(e)

def print_and_exec(script):
  print "\n==========================================================="
  print ur"【スクリプト】",
  print script
  print ur"【実行結果】"
  try:
    exec script in globals() # globals()を付けないとch9は動かない
  except Exception as e: 
    print "Error: " + str(e)
  except BaseException as e: 
    print "Error: " + str(e)

def nprint_and_exec(script):
  pass

def print_usage():
  print ur"""
from print_and_exec import *

print_and_exec(ur'''
"■ヘッダー"
Pythonスクリプト１行目
...
Pythonスクリプトｎ行目
''')
  """
