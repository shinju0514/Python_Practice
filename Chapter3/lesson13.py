
# オブジェクトのidentityを確認
scores1 = [80, 40, 50] # 同じ配列を2つ用意(リスト)
scores2 = [80 ,40, 50]
print(f'scores1のidentity: {id(scores1)}')
print(f'scores2のidentity: {id(scores2)}')
# id(変数名)
if scores1 == scores2:
    print('scores1とscores2は同じ内容です。')
else:
    print('scores1とscores2は違う内容です。')

if id(scores1) == id(scores2):
    print('scores1とscores2は同じ存在です。')
else:
    print('scores1とscores2は違う存在です。')

# identity値から参照している
# 参照をコピーしていることになる
scores1 = [80, 40, 50] # 同じ配列を2つ用意(リスト)
scores2 = [80 ,40, 50]
print(f'scores1の先頭要素は{scores1[0]}')
print(f'scores2の先頭要素は{scores2[0]}')

print('変数scores2の中身を変数scores1に代入（コピー）します。')
scores1 = scores2 # ここでscore2の参照をscore1にコピーしている

print('scores1の先頭要素を90に書き換えます。')
scores1[0] = 90 # コピーした参照が90になるため、score2の値も変わってしまう

print(f'90を代入したscores1の先頭要素は{scores1[0]}')
print(f'90を代入していないscores2の先頭要素は{scores2[0]}')

# 関数に変数の内容を書き換えられてしまう
def add_suffix(names):
    for i in range(len(names)):
        names[i] = names[i] + 'さん'
    return names

before_names = ['松田', '浅木', '工藤']
after_names = add_suffix(before_names)
print('さん付け後:' + after_names[0])
print('さん付け前:' + before_names[0])

# 防御的コピー
def add_suffix(names):
    for i in range(len(names)):
        names[i] = names[i] + 'さん'
    return names

before_names = ['松田', '浅木', '工藤']
copied_names = list()
for n in before_names:
    copied_names.append(n)
after_names = add_suffix(copied_names)
print('さん付け後:' + after_names[0])
print('さん付け前:' + before_names[0])

# identityの変化の比較
print('identityの変化を比較')

names = list() #リストの場合
print(f'list(変更前):{id(names)}')
names.append('松田')
print(f'list(変更後):{id(names)}')

name = '松田' # 文字列の場合
print(f'str(変更前):{id(name)}')
name = 'スーパー' + name
print(f'str(変更後):{id(name)}')
