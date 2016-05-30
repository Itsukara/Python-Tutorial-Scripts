# coding: UTF-8
# http://docs.python.jp/2.7/tutorial/introduction.html
# 形式ばらない Python の紹介
from print_and_exec import *
# print_usage()


print_and_exec(ur'''
"■文字列の処理"
print u'先頭にuを付けてると日本語もOK'
print ur'先頭にrを付けてると\もそのまま使える'
print u'"""か\'\'\'で囲むと複数行の文字列も使える'
print (u'+か半角空白で文字列を連結：' + "Hi " + "Tom. "
       "What a fantatic day!")
print u'*で文字列を繰り返し：'+ 3 * "Hi " + "Tom " * 2
print u'部分文字列：' + "Hi Tom"[-3:]

print '"  apple  ".strip():', "  apple  ".strip()
''')

print_and_exec(ur'''
"■タップル"
a, b = [1, 2, 3], [4, 5, 6]
t = [a + b, [7, 8, 9]]
print t
print t[0][2:5]
''')

print_and_exec(ur'''
"■while ループ"
i = 0
while i < 3:
  print u"インデントがずれるので、", (""
        u"pythonソースではTabを使わないほうがよい")
  i += 1
print u'printの最後に","を入れると',
print u'改行しない。', 
print u'ただし、","で空白が入る'
''')

