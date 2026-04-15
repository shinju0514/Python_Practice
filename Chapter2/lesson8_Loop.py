
# while 条件式:
#     条件が成立した時の処理
# 条件式が成立している間、処理を繰り返す

is_awake = True
count = 0
while is_awake == True:
    count += 1
    print(f'羊が{count}匹')
    key = input('もう眠りそうですか？(y/n)>>')
    if key == 'y':
        is_awake = False
print('おやすみなさい')

count = 0
student_num = int(input('学生の数を入力>>'))
score_list = list() # 空のリストを準備
while count < student_num:
    count += 1
    score = int(input(f'{count}人目の点数を入力>>'))
    score_list.append(score) # 入力された得点をリストに追加
print(score_list)
total = sum(score_list) # リストの合計を求める
print(f'平均点は{total / student_num}点です。')

scores = [80, 20, 75, 60]
count = 0
while count < len(scores):
    if scores[count] >= 60:
        print('合格')
    else:
        print('不合格')
    count += 1

# for 変数 in リスト:
#     繰り返し処理
scores = [80, 20, 75, 60]
for data in scores:
    if data >= 60:
        print('合格')
    else:
        print('不合格')

for num in range(10): #range() 関数で0から9までの整数の生成を実行します。
    print(num)

# 20代のサンプルデータを作成したい。サンプルとして５人まで抽出可能とする。
ages = [29, 50, 8, 20, 78, 25, 22, 10, 27, 33]
num = 5
sample = list()
for age in ages:
    if age >= 20 and age < 30:
        sample.append(age)
        if len(sample) == num:
            break #
print(sample)

age = [28, 50, '秘密', 20, 78, 25, 22, 10, '無回答', 33]
sample = list()
for data in age:
    if not isinstance(data, int):
        continue # データが整数でない場合は、以降の処理をスキップして次のループに進む
    if data >= 20 and data < 30:
        sample.append(data)
print(sample)