# 条件分岐
# コロンを忘れないよう
# name = input('あなたの名前を教えてください。>>')
# print(f'{name}さん、こんにちは')
# food = input(f'{name}さんの好きな食べ物を教えてください。')
# if food == 'カレー':
#   print('ステキです。カレーは最高ですよね。')
# else:
#   print(f'私も{food}が好きですよ')

# if 条件式:
# 条件が成立した時
# else:
# 条件が成立しなかった時
# コロンを書くことを忘れない

name = input('あなたの名前を教えてください。>>')
print(f'{name}さん、こんにちは')
food = input(f'{name}さんの好きな食べ物を教えてください。')
if 'カレー' in food: # foodの中にカレーが含まれているか判定
  print('ステキです。カレーは最高ですよね。')
else:
  print(f'私も{food}が好きですよ')

scores = [80, 90, 100, 20]
if 100 in scores: # scoresの中に100が含まれているか判定
  print('100点がありますね!')
else:
  print('次は100点を目指しましょう!')

scores = {'network': 60, 'database': 80, 'security': 50}
key = input('追加する科目名を入力してください。>>')
if key in scores: # scoresの中にkeyが含まれているか判定
  print('既に登録済です。')
else:
  data = int(input('得点を入力してください。'))
  scores[key] = data # scoresのkeyにdataを追加
print(scores)

score = int(input('試験の点数を入力>>'))
print(score >= 60)