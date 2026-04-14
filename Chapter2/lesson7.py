
# elseブロックがない分岐
name = input('あなたの名前を教えてください。>>')
print(f'{name}さんこんにちは')
if name == '松田':
    print('松田さんに会えて嬉しいです。')
food = input(f'{name}さんの好きな食べ物を教えてください。>>')
if 'カレー' in food: # foodの中に'カレー'が含まれていればTrue
    print('カレーはうまいですよね')
else:
    print(f'私も{food}が好きですよ')

# Pythonには分岐の終わりにEnd がないので注意する。
scores = int(input('試験の点数を入力してください。>>'))
if scores < 0 or scores > 100:
    print('異常な得点です。')
    print('入力し直してください。')
elif scores >= 60:
    print('合格です！')
else:
    print('不合格です。')
    print('追試を受けましょう。')

print('全ての質問にyまたはnで答えてください。')
okane_aruka = input('お金に余裕はありますか？>>')
if okane_aruka == 'y':
    onaka_suiteruka = input('お腹は空いていますか?>>')
    nomitai_kibunka = input('ビールを飲みたいですか？>>')
    if onaka_suiteruka == 'y' and nomitai_kibunka == 'y':
        print('焼肉はいかがですか')
    else:
        print('お寿司はいかがですか')
else:
    print('お家でゆっくりしましょう。')
