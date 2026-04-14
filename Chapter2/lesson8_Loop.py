
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