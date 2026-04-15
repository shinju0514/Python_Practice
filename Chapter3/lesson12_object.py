# オブジェクト.メソッド（引数・・・）

def method(str):
    print(f'{str.capitalize()}')
    print(f'{str.lower()}')
    print(f'{str.upper()}')
    print(f'{str.title()}')
    print(f'{str.strip()}')

str = 'Aaazahhh HGG'
method(str)


# userinfo = input('名前と血液型をカンマで区切って一行で出力')
# [name, blood] = userinfo.split(',')
# blood = blood.upper().strip()
# print(f'{name}さんは{blood}型なので大吉です。')


# 関数オブジェクトは変数内に代入してコピーが可能
def add(x, y):
    return x + y

type(add)
newadd = add
print(newadd(4, 5))

# 変数名 = クラス名
int_value1 = 0
int_value2 = int()
int_value3 = int(9)
list_value1 = []
list_value2 = list()
list_value3 = list(('松田', '浅木'))

list_values = [90, 50, 20]

# for lists in list_values:
#    sum = sum + lists[-1]

class Hero:
    name = '松田'
    hp = 100
    def sleep(self, hours):
        print(f'{self.name}は{hours}時間寝た')
        self.hp += hours

# ゲーム開始
print('スッキリファンタジ-')
h = Hero()
h.sleep(3)
print(f'{h.name}のHPは現在{h.hp}です')