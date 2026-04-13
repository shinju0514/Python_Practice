# input関数について　標準入力を促す
# name = input('あなたの名前を入力してください。')
# print('おお' + name + 'さん！')

# price = input('料金を入力>>')
# number = input('人数を入力>>')
# payment = price / number
# print('お支払いは' + payment + '円です。')

# このままだとstr 同士のためエラーとなる。

# 主なデータ型
# int 整数
# float 浮動小数点数
# str 文字列
# bool 真偽値

# データ型の確認
# type(変数名) で変数のデータ型を確認
x = 10
print(type(x)) # <class 'int'>
y = 3.14
print(type(y)) # <class 'float'>
z = 'Hello'
print(type(z)) # <class 'str'>
is_valid = True
print(type(is_valid)) # <class 'bool'>

print('int, float, str, bool関数について')
x = 3.14
y = int(x)
print(y)
print(type(y))
z = str(x)
print(z)
print(type(z))
print(z * 2)

price = int(input('料金を入力>>'))
number = int(input('人数を入力>>'))
payment = price / number
print('お支払いは{}円です。'.format(payment))

