# coding: UTF-8
# http://docs.python.jp/2.7/tutorial/modules.html
# 6. モジュール
from print_and_exec import *



print_and_exec(ur'''
"■6. モジュール - 1"
import os
# fibo.pyの内容を出力
os.system("type fibo.py")
''')



print_and_exec(ur'''
"■6. モジュール - 2"
import fibo

print fibo.fib(1000)
print fibo.fib2(100)
print fibo.__name__
''')



print_and_exec(ur'''
"■6. モジュール - 3"
fib = fibo.fib
print fib(500)
''')


print_and_exec(ur'''
"■6.1. モジュールについてもうすこし - 1"
from fibo import fib, fib2
print fib(500)
''')



print_and_exec(ur'''
"■6.1. モジュールについてもうすこし - 2"
from fibo import * # *を使うのはお勧めできません
print fib(500)
''')



print_and_exec(ur'''
"■6.1.1. モジュールをスクリプトとして実行する - 1"
# fibo.pyの内容を再度出力 'if __name__ == "__main__":'以降に注目
os.system("type fibo.py")
''')



print_and_exec(ur'''
"■6.1.1. モジュールをスクリプトとして実行する - 2"
os.system("python fibo.py 50")
''')



print_and_exec(ur'''
"■6.1.1. モジュールをスクリプトとして実行する - 3"
import fibo
''')


print_and_exec(ur'''
"■6.2. 標準モジュール"
import sys     
#print sys.ps1   # 対話環境でのみ有効
#print sys.ps2   # 対話環境でのみ有効
#sys.ps1 = 'C> ' # 対話環境でのみ有効

print sys.path
''')



print_and_exec(ur'''
"■6.3. dir() 関数 - 1"
import fibo, sys
print dir(fibo)
print

print dir(sys)
print
''')



print_and_exec(ur'''
"■6.3. dir() 関数 - 2"
a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
print dir()
''')



print_and_exec(ur'''
"■6.3. dir() 関数 - 3"
import __builtin__
print dir(__builtin__)  
''')



print_and_exec(ur'''
"■6.4. パッケージ - 0"
"""
# パッケージの構造例
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

 
パッケージを import する際、 Python は 
sys.path 上のディレクトリを検索して、
トップレベルのパッケージの入ったサブディレクトリを探します。
あるディレクトリを、パッケージが入ったディレクトリとして
Python に扱わせるには、ファイル __init__.py が必要です。
"""
# 以下は、次以降の例で使うユーティリティ関数と変数
import sys
def del_module(module_name):
  sub_names = module_name.split(".")
  for i in range(0, len(sub_names)):
    sub_name = ".".join(sub_names[0:i+1])
    if sub_name in  sys.modules:
      del sys.modules[sub_name]

input  = "INPUT.data"
output = "OUTPUT.data"
''')


print_and_exec(ur'''
"■6.4. パッケージ - 1"
#echo.pyの中身を以下で出力
os.system(r"type sound\effects\echo.py")
''')


print_and_exec(ur'''
"■6.4. パッケージ - 2"
import sound.effects.echo
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

del_module('sound.effects.echo')
''')


print_and_exec(ur'''
"■6.4. パッケージ - 3"
from sound.effects import echo
echo.echofilter(input, output, delay=0.7, atten=4)

del_module('sound.effects.echo')
''')


print_and_exec(ur'''
"■6.4. パッケージ - 4"
from sound.effects.echo import echofilter
echofilter(input, output, delay=0.7, atten=4)

del_module('sound.effects.echo')
''')


print_and_exec(ur'''
"■6.4.1. パッケージから * を import する - 1"
#sound\effects\__init__.pyの中身を以下で出力
os.system(r"type sound\effects\__init__.py")
''')


print_and_exec(ur'''
"■6.4.1. パッケージから * を import する - 2"
import sound.effects.echo
import sound.effects.surround
from sound.effects import *

del_module('sound.effects.echo')
del_module('sound.effects.surround')
''')


print_and_exec(ur'''
"■6.4.2. パッケージ内参照"
#sound\effects\surround.pyの中身を以下で出力
os.system(r"type sound\effects\surround2.py")
print

import sound.effects.surround2
print sound.formats.__all__

del_module('sound.effects.surround2')
del_module('sound.effects.echo')
del_module('sound.formats')
del_module('sound.effects.equalizer')
''')


print_and_exec(ur'''
"■おまけ"
os.system(r"type sound\effects\__init__.py")

import sound.formats.wavread
print sound.formats.wavread.read("test1.wav") # full name
del_module('sound.formats.wavread'); print

from sound.formats import wavread
print wavread.read("test2.wav") # module.function
del_module('sound.formats.wavread'); print

from sound.formats.wavread import read
print read("test3.wav")         # function
del_module('sound.formats.wavread'); print

from sound.formats.wavread import *
print readall()                 # function
del_module('sound.formats.wavread'); print

# import sound.formats.wavread.readall # Error (last one must be module)

import sound.formats.auread
from sound.formats import * # effective only for already imported module
                            # or included in __all__ set in __ini__.py
print auread.read("test2.au")
''')