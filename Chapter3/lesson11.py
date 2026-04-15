# global文を用いてグローバル変数に代入する

name = '松田'
def change_name():
    global name # この関数におけるnameはグローバル変数であると宣言
    name = '浅木'
def hello():
    print(f'こんにちは{name}さん')

change_name()
hello()

# 練習
def weather():
    print('今日は晴れです。')
weather()
# radius (半径)
def calc_circle_ares(radius: int):
    return radius * 3.14

calc = calc_circle_ares(5)  # radius (radius) = 4
print(calc)
