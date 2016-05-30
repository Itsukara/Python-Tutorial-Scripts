# coding: UTF-8
# http://docs.python.jp/2.7/tutorial/introduction.html
# 形式ばらない Python の紹介
from print_and_exec import *


print_and_exec(ur'''
"■Namespace"
v = 100
w = 200
x = [300]
def func(a = v, b = x):
  global w
  # print v # Error: local variable 'v' referenced before assignment
  v = 10
  if a == 150:
    w = 20
  print "a={:<5d}, b={:6s}, v={:<5d}, w={:<5d}, x={:6s}".format(a, b, v, w, x)

func()

v = 1000
func(150)

w = 2000
func()

x[0] = 3000
func()
''')



print_and_exec(ur'''
"■Class Intro"
# 下記で"object"が抜けると旧classになり、下記のエラーが出る
#   TypeError: must be type, not classobj
class Complex(object):
  _imagstr = "i" # class変数、先頭に"_"を付けprivate扱いと表示
  _seqnum  = 0   # class変数、先頭に"_"を付けprivate扱いと表示
  def __init__(self, realpart, imagpart):
    self._r = realpart
    self._i = imagpart
    self._id = Complex._seqnum
    Complex._seqnum += 1
  def add(self, c):
    if not isinstance(c, Complex): raise TypeError(repr(c)+" is not Complex")
    r1 = self._r; i1 = self._i
    r2 = c._r   ; i2 = c._i
    return Complex(r1+r2, i1+i2)
  def mul(self, c):
    if not isinstance(c, Complex): raise TypeError(repr(c)+" is not Complex")
    r1 = self._r; i1 = self._i
    r2 = c._r   ; i2 = c._i
    return Complex(r1*r2 - i1*i2, r1*i2 + i1*r2)
  def tostring(self, typestr="Complex"):
    # None判定はisかis notで行う必要がある
    tag = "{};@{} ".format(typestr, self._id) if typestr is not None else ""
    return "[{}{} + {}{}]".format(tag, self._r, self._i, self._imagstr)

c1 = Complex(0,   1)
c2 = Complex(-1, -1)
cadd = c1.add(c2)
cmul = c1.mul(c2)
cxxx = Complex.mul(c1, c2)
print 'c1={}, c2={}'.format(c1.tostring(None), c2.tostring(None))
print 'c1+c2={}'.format(cadd.tostring())
print 'c1*c2={}'.format(cmul.tostring())
print 'c1*c2={}'.format(cxxx.tostring())

try_exec("c1.add(1.0)") # TypeError
''')



print_and_exec(ur'''
"■Inheritance"
class IntComplex(Complex):
  def __init__(self, realpart, imagpart):
    if not isinstance(realpart, int) or not isinstance(imagpart, int) :
       raise TypeError("realpart or imagpart is not int")
    super(IntComplex, self).__init__(realpart, imagpart)
  def add(self, c):
    if not isinstance(c, IntComplex): raise TypeError(repr(c)+" is not IntComplex")
    r = Complex.add(self, c)
    return IntComplex(r._r, r._i) # Python don't have function "class cast"
  def mul(self, c):
    if not isinstance(c, Complex): raise TypeError(repr(c)+" is not IntComplex")
    r = Complex.mul(self, c)
    return IntComplex(r._r, r._i) # Python don't have function "class cast"
  def tostring(self, typestr="IntComplex"):
    return super(IntComplex, self).tostring(typestr)

c1 = IntComplex(0,   1)
c2 = IntComplex(-1, -1)
cadd = c1.add(c2)
cmul = c1.mul(c2)
cxxx = IntComplex.mul(c1, c2)
print 'c1={}, c2={}'.format(c1.tostring(None), c2.tostring(None))
print 'c1+c2={}'.format(cadd.tostring())
print 'c1*c2={}'.format(cmul.tostring())
print 'c1*c2={}'.format(cxxx.tostring())

try_exec("IntComplex(1.0, 1)") # TypeError
try_exec("IntComplex(1, 1.0)") # TypeError

cr = Complex(1, 1)
ca1 = cr.add(c1)
print ca1.tostring() 

try_exec("ca2 = c1.add(cr)") # TypeError
''')



print_and_exec(ur'''
"■Inheritance Basics"
"""
・「self.変数名」に代入するとインスタンス変数が作成される
・インスタンス変数作成前は「self.変数名」はクラス変数を参照
・参照方法による参照変数の違い
 (1)クラス名.変数名       (必ずクラス変数にアクセスする)
 (2)self.__class__.変数名 (文脈(selfの値)によって変わる)
 (3)self.変数名           (文脈と、インスタンス変数生成前後で変わる)
・指針
 (a)クラス変数とインスタンス変数は異なった名称を使うのが良い
 (b)クラス変数は(1)でアクセスするのが良い
 (c)インスタンス変数は(3)でアクセスするのが良い
"""
class A(object):
  myname = "A"
  def __init__(self):
    print "A.__init_"
    self.update() # call overrided method
  def update(self):
    print "A.update"
    print "A.myname              ="+A.myname
    print "self.__class__.myname ="+self.__class__.myname
    print "self.myname           ="+self.myname # 初回はクラス変数、途中からインスタンス変数
  def update_names(self):
    print "A.update_names"
    self.myname = "Instance of A" # インスタンス変数が生成される
    A.myname    = "Class A"       # class変数への値設定
x = A()
print
x.update_names()
x.update()
print

class B(A):
  myname = "B"
#  A.__init__ will be called
  def update(self):
    print "B.update"
    print "B.myname              ="+B.myname
    print "self.__class__.myname ="+self.__class__.myname
    print "self.myname           ="+self.myname # 初回はクラス変数、途中からインスタンス変数
  def update_names(self):
    print "B.update_names"
    self.myname = "Instance of B" # インスタンス変数が生成される
    B.myname    = "Class B"       # class変数への値設定
x = B()
print
x.update()
print
x.update_names()
x.update()
print

class C(A):
  myname = "C" # 
  def __init__(self):
    # A._init__は呼び出されない
    print "C.__init__"
    self.update()
  def update_names(self):
    print "C.update_names"
    self.myname = "Instance of C" # インスタンス変数が生成される
    C.myname    = "Class C"       # class変数への値設定
x = C()
print
x.update_names()
x.update()
print

class D(A):
  myname = "D"
  def __init__(self):
    super(D, self).__init__()
    print "D.__init__"
  def update(self):
    print "D.update"
    print "D.myname              ="+D.myname
    print "self.__class__.myname ="+self.__class__.myname
    print "self.myname           ="+self.myname # 初回はクラス変数、途中からインスタンス変数
  def update_names(self):
    print "D.update_names"
    self.myname = "Instance of D" # インスタンス変数が生成される
    D.myname    = "Class D"       # class変数への値設定
x = D()
print
x.update()
print
x.update_names()
x.update()
print

A(); print
B(); print
C(); print
D(); print
''')



print_and_exec(ur'''
"■Private Variables and Class-local References"
"""
オブジェクトの中からしかアクセス出来ない
“プライベート” インスタンス変数は、 Python にはありません。
しかし、ほとんどの Python コードが従っている慣習があります。
アンダースコアで始まる名前 (例えば _spam) は、
 (関数であれメソッドであれデータメンバであれ) 
 非 public なAPI として扱います。
 これらは、予告なく変更されるかもしれない実装の詳細として扱われるべきです。

クラスのプライベートメンバについて適切なユースケース
(特にサブクラスで定義された名前との衝突を避ける場合)
があるので、マングリング(name mangling) と呼ばれる、
限定されたサポート機構があります。 
__spam (先頭に二個以上の下線文字、末尾に一個以下の下線文字)
という形式の識別子は、 _classname__spam へとテキスト置換
されるようになりました。
ここで classname は、現在のクラス名から先頭の下線文字を
はぎとった名前になります。このような難号化 (mangle) は、
識別子の文法的な位置にかかわらず行われるので、
クラス定義内に現れた識別子全てに対して実行されます。

名前のマングリングは、サブクラスが内部のメソッド呼び出しを
壊さずにメソッドをオーバーライドするのに便利です。例えば:
"""

class A(object):
  def __init__(self):
    print "A.__init_"
    self.__update()
  def update(self):
    print "A.update"
  __update = update # private copy of original update() method

class D(A):
  def __init__(self):
    super(D, self).__init__()
    print "D.__init__"
  def update(self): # does not break __init__()
    print "B.update"
x = D()
x.update()

"""
(補足)
・Pythonには、メソッドのオーバーロードは無い
・サブクラスでのメソッド・オーバライドはある
・キャストが無いので、ポリモーフィズムとは無縁
・コンストラクタ__init__()の自動挿入はない
・スーパークラスのコンストラクタ__init__()の呼び出し自動挿入もない
・スタティックイニシャライザーも無い
・finalが無い
・private、protectedなども無い(全てpublic)
"""
''')



print_and_exec(ur'''
"■Odds and Ends"
"""
Pascal の “レコード (record)” や、
C 言語の “構造体 (struct)” のような、
名前つきのデータ要素を一まとめにするデータ型があると便利なことがあります。
空のクラス定義を使うとうまくできます:
(追記)
オブジェクトをstringに変換する関数も必要と思われるので追加した
"""

def tostr(self):
    attributes = {name:object.__getattribute__(self, name)
                     for name in dir(self) if name[0:2] != "__"}
    return str(attributes)

def torepr(self):
    attributes = {name:object.__getattribute__(self, name) 
                    for name in dir(self) if name[0:2] != "__"}
    return repr(attributes)

class Employee(object):
  __str__ = tostr
  __repr__ = torepr

john = Employee() # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000.5

print john
print tostr(john)
print torepr(john)
''')



print_and_exec(ur'''
"■寄り道"
"""
objectのいくつかの特殊メソッドを上書きして試す。
色々と決まり事あるらしい

・クラスが __cmp__() や __eq__() メソッドを定義していない場合、 
  __hash__() メソッドも定義してはなりません
・クラスが __cmp__() または __eq__() を定義しているが、 
  __hash__() を定義していない場合、インスタンスを辞書の
  キーとして使うことはできません。
・クラスが変更可能なオブジェクトを定義しており、 
  __cmp__() または __eq__() メソッドを実装している場合、 
  __hash__() を定義してはなりません。
"""

class Human(object):
  __str__ = tostr   # String化は「Odds and Ends」で定義したものを流用
  __repr__ = torepr # String化は「Odds and Ends」で定義したものを流用 
  def __init__(self, name, age):
    self._name = name
    self._age  = age
  def __cmp__(self, other):
    if not isinstance(other, Human): raise TypeError(repr(other)+" is not Human")
    return self._age - other._age
# 下記、定義しなくても何故かうまくいくが... 一応定義しておく
  def __hash__(self): 
    return hash(self._name)*31 + self._age

john = Human("John", 39)
bill = Human("Bill", 21)
print "john="+str(john)
print "bill="+str(bill)
print

print john > bill
try_exec("print john > 29") # Exception
print

# Human型をキーとする辞書を作成してみる
hdec = {john:"American", bill:"Canadian"}
hdec.update({Human("Tom", 29):"Chinese", Human("Jim", 44):"Korean"})
hdec[john] = "Japanese";
print hdec
print

if hdec: print "TRUE" # Human.__nonzero__が未定義なので必ずTrue
''')



print_and_exec(ur'''
"■Generator"
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('Abracadabra'):
    print char,
print
print

print sum(i*i for i in range(10))   
print

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print sum(x*y for x,y in zip(xvec, yvec)) 
print

from math import pi, sin
sine_table = dict((x, sin(x*pi/180)) for x in range(0, 91, 10))
print sine_table
print

text = """
Some simple generators can be coded succinctly as expressions 
using a syntax similar to list comprehensions but with parentheses 
instead of brackets. These expressions are designed for situations 
where the generator is used right away by an enclosing function. 
Generator expressions are more compact but less versatile than 
full generator definitions and tend to be more memory friendly 
than equivalent list comprehensions.
"""
page = text.split("\n")
unique_words = set(word  for line in page  for word in line.split())
print unique_words
''')
