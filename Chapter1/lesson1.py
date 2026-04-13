# 変数について
name = '松田'
age = 22
print(name)
print(age)

print('半径が3cmの円の直径は、')
dia = 3 * 2
print(dia)
print('その円の円周の長さは、')
print(dia * 3.14)

# python　には予約語は使用できない。アンダースコアを二つ繋げた名前も使用できない。
# 小文字で始まるわかりやすい変数名が望ましい

# 変数の上書き
count = 3
print('今日カレーを食べた回数は')
print(count)
count = 5 # ここで上書き
print('本当は')
print(count)

# まとめて変数を定義
name, age = '浅木',24 # カンマをつけて複数定義できる

# 複合代入演算子
age = 24
age += 1 # age = age + 1　と同じ

price = 2600
price *= 1.5 # price = price * 1.5 と同じ

