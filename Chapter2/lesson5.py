# ディクショナリの作成
# 変数 = {キー1: 値1, キー2: 値2, ...}
scores = {'network': 60, 'database': 80, 'security':50}
print(scores)
print(scores['database'])

scores = {'network': 60, 'database': 80, 'security':50}
scores['programming'] = 65 # ディクショナリの要素を追加
scores['security'] = 55    # ディクショナリの要素を変更
print(scores)

del scores['security'] # del文でディクショナリの要素を削除
print(scores)

# sum関数と.values()メソッドでディクショナリの値の合計を求めることができます。
scores = {'network': 60, 'database': 80, 'security':50}
total = sum(scores.values()) # ディクショナリの値の合計を求める)
print(total)

# タプルの利用
scores = (60, 80, 55)
print(scores)
print(scores[0])
print(f'要素数は{len(scores)}')
print(f'合計は{sum(scores)}')
# 定義後に要素を変更することはできない。
# scores[0] = 70 エラーが発生する

# リストの型
member = ['松田']
print(type(member))

# タプルの型
member = ('松田')
print(type(member))
# タプルを定義する際は、要素が1つの場合でもカンマを付ける必要があります。
member = ('松田',)
print(type(member))

# セットの定義
# 変数 = {要素1, 要素2, ...}
scores = {70, 80, 44, 80} # セットは重複する要素を持つことができないため、80は1つしか存在しません。
scores.add(80) # セットに要素を追加する
print(scores)
print(f'要素数は{len(scores)}')
print(f'合計は{sum(scores)}')# 80は重複しない

# コンテナの相互変換
scores = {'network': 60, 'database': 80, 'security': 60}
members = ['松田', '浅木', '工藤']
print(tuple(members)) # タプルに変換
print(list(scores)) # リストに変換
print(set(scores.values())) # セットに変換　ディクショナリの値をセットに変換するため、重複する値は1つしか存在しません.

# ディクショナリの中にディクショナリをネスト
matsuda_scores = {'network': 60, 'database': 80, 'security': 50}
asagi_scores = {'network': 70, 'database': 90, 'security': 55}
member_scores = {
  '松田': matsuda_scores, # ディクショナリを値として使用することができます。
  '浅木': asagi_scores
}
print(member_scores)

member_hobbies = {
  '松田': {'SNS', '麻雀', '自転車'},
  '浅木': {'麻雀', '食べ歩き', '数学', '数学'}
}
# 全員の趣味一覧を表示
print(member_hobbies)
# 松田の趣味を表示
print(member_hobbies['松田']) # キーを指定する
# 浅木の趣味を表示
print(member_hobbies['浅木'])

# ２次元リスト
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]

print(c) # リストC全体を参照
print(c[0]) # リストcの0番目を参照
print(c[1][2]) # リストcの1番目のリストの2番目を参照

# 集合演算子
member_hobbies = {
  '松田': {'SNS', '麻雀', '自転車'},
  '浅木': {'麻雀', '食べ歩き', '数学', '数学'}
}
common_hobbies = member_hobbies['松田'] & member_hobbies['浅木']
# 二人に共通する趣味一覧を表示
print(common_hobbies)

A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
print(A | B) # AとBの和集合を表示
print(A & B) # AとBの積集合を表示
print(A - B) # AからBを引いた差集合を表示
print(A ^ B) # AとBの対称差集合を表示

# 問題
scores = []
scores.append(int(input('国語の点数>>')))
scores.append(int(input('数学の点数>>')))
scores.append(int(input('英語の点数>>')))
scores.append(int(input('理科の点数>>')))
scores.append(int(input('社会の点数>>')))
total = (f'合計点は{sum(scores)}点です。平均点は{sum(scores)/ len(scores)}点です。')
print(total)