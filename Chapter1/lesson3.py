# format関数
name = '松田公太'
age = 23
height = 175.6
print('私の名前は{}です。年齢は{}歳で、身長は{}cmです。'.format(name, age, height))
# format関数で上から順番に変数を指定することができます。

# f-string
print(f'私の名前は{name}です。年齢は{age}歳で、身長は{height}cmです。')
print(f'私の名前は{name}です。年齢は{age}歳で、身長は{height / 100}mです。')