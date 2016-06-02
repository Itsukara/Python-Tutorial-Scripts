# coding: UTF-8
# http://docs.python.jp/2.7/tutorial/introduction.html
# 3. 形式ばらない Python の紹介
from print_and_exec import *
# print_usage()


print_and_exec(ur'''
"■3.1.1. 数 - 1"
print 2 + 2
print 50 - 5*6
print (50 - 5.0*6) / 4
print 8 / 5.0
''')


print_and_exec(ur'''
"■3.1.1. 数 - 2"
print 17 / 3     # int / int -> int
print 17 / 3.0   # int / float -> float
print 17 // 3.0  # explicit floor division discards the fractional part
print 17 % 3     # the % operator returns the remainder of the division
print 5 * 3 + 2  # result * divisor + remainder
''')


print_and_exec(ur'''
"■3.1.1. 数 - 3"
print 5 ** 2  # 5 squared
print 2 ** 7  # 2 to the power of 7
''')


print_and_exec(ur'''
"■3.1.1. 数 - 4"
width = 20
height = 5 * 9
print width * height
''')


print_and_exec(ur'''
"■3.1.1. 数 - 5"
n  # try to access an undefined variable
''')


print_and_exec(ur'''
"■3.1.1. 数 - 6"
print 3 * 3.75 / 1.5
print 7.0 / 2
''')


print_and_exec(ur'''
"■3.1.1. 数 - 7"
tax = 12.5 / 100
price = 100.50
print price * tax
try_exec("print price + _")   # 対話モードではないので"_"は使えない
try_exec("print round(_, 2)") # 対話モードではないので"_"は使えない 
''')


print_and_exec(ur'''
"■3.1.2. 文字列(原文) - 1"
print repr('spam eggs')  # single quotes
print repr('doesn\'t')   # use \' to escape the single quote...
print repr("doesn't")    # ...or use double quotes instead
print repr('"Yes," he said.')
print repr("\"Yes,\" he said.")
print repr('"Isn\'t," she said.')
''')


print_and_exec(ur'''
"■3.1.2. 文字列(原文) - 2"
print repr('"Isn\'t," she said.')
print      '"Isn\'t," she said.'
s = 'First line.\nSecond line.'  # \n means newline
print repr(s) # without print, \n is included in the output
print s       # with print, \n produces a new line
''')


print_and_exec(ur'''
"■3.1.2. 文字列(原文) - 3"
print 'C:\some\name'  # here \n means newline!
print r'C:\some\name' # note the r before the quote
''')


print_and_exec(ur'''
"■3.1.2. 文字列(原文) - 4"
print """\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""
''')


print_and_exec(ur'''
"■3.1.2. 文字列(原文) - 5"
# 3 times 'un', followed by 'ium'
print repr(3 * 'un' + 'ium')
''')


print_and_exec(ur'''
"■3.1.2. 文字列(原文) - 6"
print repr('Py' 'thon')
''')


print_and_exec(ur'''
"■3.1.2. 文字列(原文) - 7"
text = ('Put several strings within parentheses '
        'to have them joined together.')
print repr(text)
''')


print_and_exec(ur'''
"■3.1.2. 文字列(原文) - 8"
word = 'Python'
print repr(word[0]) # character in position 0
print repr(word[5]) # character in position 5
''')


print_and_exec(ur'''
"■3.1.2. 文字列(原文) - 9"
print repr(word[-1])
print repr(word[-2])
print repr(word[-6])
''')


print_and_exec(ur'''
"■3.1.2. 文字列(原文) - 10"
print repr(word[0:2])
print repr(word[2:5])
''')


print_and_exec(ur'''
"■3.1.2. 文字列(原文) - 11"
print repr(word[:2] + word[2:])
print repr(word[:4] + word[4:])
''')


print_and_exec(ur'''
"■3.1.2. 文字列(原文) - 12"
print repr(word[:2])  # character from the beginning to position 2 (excluded)
print repr(word[4:])  # characters from position 4 (included) to the end
print repr(word[-2:]) # characters from the second-last (included) to the end
''')


print_and_exec(ur'''
"■3.1.2. 文字列(原文) - 13"
print repr(word[42]) # the word only has 6 characters (Error)
''')


print_and_exec(ur'''
"■3.1.2. 文字列(原文) - 14"
print repr(word[4:42]) # not Error
print repr(word[42:])  # not Error
''')


print_and_exec(ur'''
"■3.1.2. 文字列(原文) - 15"
try_exec("word[0] = 'J'")
try_exec("word[2:] = 'py'")
''')


print_and_exec(ur'''
"■3.1.2. 文字列(原文) - 16"
print repr('J' + word[1:])
print repr(word[:2] + 'py')
''')


print_and_exec(ur'''
"■3.1.2. 文字列(原文) - 17"
s = 'supercalifragilisticexpialidocious'
print len(s)
''')


print_and_exec(ur'''
"■3.1.3. Unicode 文字列 - 1"
print repr(u'Hello World !')
''')


print_and_exec(ur'''
"■3.1.3. Unicode 文字列 - 2"
print repr(u'Hello\u0020World !')
''')


print_and_exec(ur'''
"■3.1.3. Unicode 文字列 - 3"
print repr(ur'Hello\u0020World !')
print repr(ur'Hello\\u0020World !')
''')


print_and_exec(ur'''
"■3.1.3. Unicode 文字列 - 4"
print repr(u"abc")
print repr(str(u"abc"))
# 欧州文字がスクリプトのプリントでエラーになるので削除
# 欧州文字がスクリプトのプリントでエラーになるので削除
''')

print_and_exec(ur'''
"■3.1.3. Unicode 文字列 - 5"
# 欧州文字がスクリプトのプリントでエラーになるので削除
''')


print_and_exec(ur'''
"■3.1.4. リスト(原文) - 1"
squares = [1, 4, 9, 16, 25]
print squares
''')


print_and_exec(ur'''
"■3.1.4. リスト(原文) - 2"
print squares[0]    # indexing returns the item
print squares[-1]
print squares[-3:]  # slicing returns a new list
''')


print_and_exec(ur'''
"■3.1.4. リスト(原文) - 3"
print squares[:]
''')


print_and_exec(ur'''
"■3.1.4. リスト(原文) - 4"
print squares + [36, 49, 64, 81, 100]
''')


print_and_exec(ur'''
"■3.1.4. リスト(原文) - 5"
cubes = [1, 8, 27, 65, 125]  # something's wrong here
print 4 ** 3   # the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
print cubes
''')


print_and_exec(ur'''
"■3.1.4. リスト(原文) - 6"
cubes.append(216)     # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print cubes
''')


print_and_exec(ur'''
"■3.1.4. リスト(原文) - 7"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print letters
# replace some values
letters[2:5] = ['C', 'D', 'E']
print letters
# now remove them
letters[2:5] = []
print letters
# clear the list by replacing all the elements with an empty list
letters[:] = []
print letters
''')


print_and_exec(ur'''
"■3.1.4. リスト(原文) - 8"
letters = ['a', 'b', 'c', 'd']
print len(letters)
''')


print_and_exec(ur'''
"■3.1.4. リスト(原文) - 9"
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print x
print x[0]
print x[0][1]
''')


print_and_exec(ur'''
"■3.2. プログラミングへの第一歩 - 1"
# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while b < 10:
    print b
    a, b = b, a+b
''')


print_and_exec(ur'''
"■3.2. プログラミングへの第一歩 - 2"
i = 256*256
print 'The value of i is', i
''')


print_and_exec(ur'''
"■3.2. プログラミングへの第一歩 - 3"
a, b = 0, 1
while b < 1000:
    print b,       # 改行しない
    a, b = b, a+b
''')


print_and_exec(ur'''
"■おまけ　文字列の処理"
print u'先頭にuを付けてると日本語もOK'
print ur'先頭にrを付けてると\もそのまま使える'
print u'"""か\'\'\'で囲むと複数行の文字列も使える'
print (u'+か半角空白で文字列を連結：' + "Hi "   "Tom. "
       "What a fantatic day!")
print u'*で文字列を繰り返し：'+ 3 * "Hi " + 2 * "Tom "
print u'部分文字列：' + "Hi Tom"[-3:]

print '"  apple  ".strip():', "  apple  ".strip()
''')

print_and_exec(ur'''
"■おまけ　リスト"
a, b = [1, 2, 3], [4, 5, 6]
t = [a + b, [7, 8, 9]]
print t
print t[0][2:5]
''')

print_and_exec(ur'''
"■おまけ　while ループ"
i = 0
while i < 3:
  print (u"インデントがずれるので、"
         u"pythonソースではTabを使わないほうがよい")
  i += 1
print u'printの最後に","を入れると',
print u'改行しない。', 
print u'ただし、","で空白が入る'
''')

