# coding: UTF-8
# http://docs.python.jp/2.7/tutorial/introduction.html
# 形式ばらない Python の紹介
from print_and_exec import *



print_and_exec(ur'''
"■Module"
import fibo

fibo.fib(1000); print

print fibo.fib2(100)
print fibo.__name__

fib = fibo.fib
fib(500); print

from fibo import fib, fib2
# from fibo import * # not recommended
fib(500); print
''')



print_and_exec(ur'''
"■Standard Modules"
import sys

# print sys.ps1, sys.ps2 # effective only in interactive environment
import fibo
print sys.path; print
print dir(fibo); print
print dir(sys); print
print dir(); print
''')



print_and_exec(ur'''
"■Packages"
"""
# パッケージの構造例
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
# パッケージを import する際、 Python は 
# sys.path 上のディレクトリを検索して、
# トップレベルのパッケージの入ったサブディレクトリを探します。
# あるディレクトリを、パッケージが入ったディレクトリとして
# Python に扱わせるには、ファイル __init__.py が必要です。
"""
import sound.formats.wavread
print sound.formats.wavread.read("test1.wav") # full name

from sound.formats import wavread
print wavread.read("test2.wav") # module.function

from sound.formats.wavread import read
print read("test3.wav")         # function

from sound.formats.wavread import *
print readall()                 # function

# import sound.formats.wavread.readall # Error (last one must be module)

import sound.formats.auread
from sound.formats import * # effective only for already imported module
                            # or included in __all__ set in __ini__.py
print auread.read("test2.au")
''')