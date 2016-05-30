# coding: UTF-8
# http://docs.python.jp/2.7/tutorial/introduction.html
# 形式ばらない Python の紹介
from print_and_exec import *



print_and_exec(ur'''
"■if statement - alternative for switch too"
"""
Pythonにはif文はあるが、switchやcaseはない。
if文をswitchのように使う。
"""

#x = int(raw_input('Input x as number :')) #
x = 1
if x == 0:
  print 'Zero'
elif x == 1:
  print 'One'
elif x == 2:
  print 'Two'
else:
  print 'Others'
''')



print_and_exec(ur'''
"■for loop - range(len(words))"
words = ['Mary', 'had', 'a', 'little', 'lamb']
for w in words:
  print w, len(w)
  
print "------------"
for i in range(len(words))[1:4]:
  print i, words[i]
  
print "------------"
for n in range(2, 10):
  for x in range(2, (n)/2+1):
    if n % x == 0:
      print n, 'equals', x, '*', n/x
      break
  else:
    # loop fell through without finding a factor
    print n, 'is a prime number'
''')



print_and_exec(ur'''
"■pass - placeholder"
"""
pass 文は何もしません。
pass は、文を書くことが構文上要求されているが、
プログラム上何の動作もする必要がない時に使われます:

最小のクラスを作るときによく使われます。
"""
class MyEmptyClass:
  pass
"""
pass が使われるもう1つの場所は、
新しいコードを書いている時の関数や条件文の中身です。
こうすることで、具体的なコードを書かないで
抽象的なレベルで考えることができます。
"""
def initlog(*args):
  pass   # Remember to implement this!
''')



print_and_exec(ur'''
"■def - no return value (None is returned)"
def fib(n):    # write Fibonacci series up to n
  """Print a Fibonacci series up to n (docstring)."""
  a, b = 0, 1
  while a < n:
    print a,
    a, b = b, a+b
  print
f = fib
f(2000)

"""
(注)関数の中では、グローバルな変数を参照することはできますが、
    直接値を代入することはできません。
      (代入するとローカル変数となるため)
      (global 文で名前を挙げておけば可能)
"""
''')



print_and_exec(ur'''
"■def - return value"
def fib2(n): # return Fibonacci series up to n
  """Return a list containing the Fibonacci series up to n."""
  result = []
  a, b = 0, 1
  while a < n:
    result.append(a)    # see below
    a, b = b, a+b
  return result

f100 = fib2(100)        # call it
print f100              # write the result
''')



print_and_exec(ur'''
"■def - default argument value"
i = 5
def f(arg=i):
    print arg
i = 6
f()
''')



print_and_exec(ur'''
"■def -  warning to default argument value"
"""
重要な警告: デフォルト値は 1 度だけしか評価されません。
デフォルト値がリストや辞書のような変更可能なオブジェクト
の時にはその影響がでます：
"""
def f(a, L=[]):
    L.append(a)
    return L
print f(1)
print f(2)
print f(3)
print

"これを回避するには下記のように書きます。"
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print f(1)
print f(2)
print f(3)
''')



print_and_exec(ur'''
"■def - keyword argument"
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "voltage={}, state={}, action={}, type={}".format(
            voltage, state, action, type)

parrot(1000)                                          # 1 positional argument
print
parrot(voltage=1000)                                  # 1 keyword argument
print
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
print
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
print
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
print
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword''')



print_and_exec(ur'''
"■def - map argument"
def cheeseshop(kind, *arguments, **keywords):
    print "kind={}".format(kind)

    print "arguments=",
    for arg in arguments:
        print arg,
    print

    print "keywords=",
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw], ", ",
    print

cheeseshop("kind1", 
           "arg1", "arg2", "arg3",
           kw1='value1',
           kw2="value2",
           kw3="value3")
''')



print_and_exec(ur'''
"■def - unpacked argument list"
print range(3, 6)             # normal call with separate arguments
args = [3, 6]
print range(*args)            # call with arguments unpacked from a list
''')



print_and_exec(ur'''
"■def - unpack map argument"
def parrot(voltage, state='a stiff', action='voom'):
    print "voltage={}".format(voltage)
    print "state  ={}".format(state)
    print "action ={}".format(action)

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
''')



print_and_exec(ur'''
"■lambda expression"
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
print f(0)
print f(10)
''')



print_and_exec(ur'''
"■def - documentation string"
"""
最初の行は、常に対象物の目的を短く簡潔にまとめたものでなくてはなりません。
最初の行は大文字で始まり、ピリオドで終わっていなければなりません。
さらに記述すべき行がある場合、二行目は空行にし、
まとめの行と残りの記述部分を視覚的に分離します。
つづく行は一つまたはそれ以上の段落で、
対象物の呼び出し規約や副作用について記述します
"""

def my_function():
    """Do nothing, but document it.
    
    No, really, it doesn't do anything.
    """
    pass
print my_function.__doc__
''')



print_and_exec(ur'''
"■coding style"
"""
・インデントには空白 4 つを使い、タブは使わないこと。
　空白 4 つは (深くネストできる) 小さいインデントと
　 (読み易い) 大きいインデントのちょうど中間に当たります。
　タブは混乱させるので、使わずにおくのが良いです。

・ソースコードの幅が 79 文字を越えないように行を折り返すこと。
　こうすることで小さいディスプレイを使っているユーザも読み易くなり、
　大きなディスプレイではソースコードファイルを並べることもできるようになります。

・関数やクラスや関数内の大きめのコードブロックの区切りに空行を使いなさい。

・可能なら、コメントは行に独立で書きなさい

・docstring を使いなさい。

・演算子の前後とコンマの後には空白を入れ、
  括弧類のすぐ内側には空白を入れないこと: 
　a = f(1, 2) + g(3, 4)。

・クラスや関数に一貫性のある名前を付けなさい。
　慣習では CamelCase をクラス名に使い、
　lower_case_with_underscores を関数名やメソッド名に使います。
　常に self をメソッドの第 1 引数の名前 (クラスやメソッド
　についてはクラス初見 を見よ) として使いなさい。

・あなたのコードを世界中で使ってもらうつもりなら、
　風変りなエンコーディングは使わないこと。
　どんな場合でも、プレーン ASCII が最も上手くいきます。
"""
''')

