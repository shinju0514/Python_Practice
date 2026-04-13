# リストについて　（配列のようなもの）
member = ['工藤', '松田', '浅木']
print(member)
print(member[0])

scores = [88, 90, 95]
total = scores[0] + scores[1] + scores[2]
print(f'合計{total}点')

# sum関数を使用して合計を求めることもできます。
# total = sum(scores)
# print(f'合計{total}点')

# len関数で要素数を求めてavgで平均を求める
scores = [88, 90, 95]
total = sum(scores)
avg = total / len(scores)
print(f'合計{total}点、平均{avg}点')

# members関数で指定した要素をリストに追加できる
members = ['工藤', '松田', '浅木']
members.append('菅原')
members.append('湊')
members.append('朝霞')
print(members)

# リスト.remove()で指定した要素をリストから削除できる
members = ['工藤', '松田', '浅木']
members.remove('松田')
print(members)

members = ['工藤', '松田', '浅木']
members[0] = '菅原' # リストの0番目の要素を'菅原'に変更する
print(members)

# sliceによる範囲指定
a = [10, 20, 30, 40, 50]
print(a[1:3]) # 添字が１以上３未満の要素を取得
print(a[2:])  # 添字が２以上の全ての要素を取得
print(a[:3])  # 添字が３未満の全ての要素を取得
print(a[-1])  # 末尾の要素を取得
print(a[-2])  # 末尾から2番目の要素を取得
