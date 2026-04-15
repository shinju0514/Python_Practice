# 関数の定義
def hello(name): # 仮引数nameを設定
    print(f'こんにちは{name}です。')

hello('浅木') # 呼び出す時は実引数
hello('松田')

# 複数の仮引数を定義
def profile(name, age, hobby):
    print(f'私の名前は{name}です。')
    print(f'年齢は{age}歳です。')
    print(f'趣味は{hobby}です。')

def calc_average(scores):
    avg = sum(scores) / len(scores)
    print(f'平均点は{avg}点です。')

score = [90, 20, 100, 22, 99, 54]
calc_average(score)

# def 関数名(引数1, 引数2, ...):
#     処理
#     return 戻り値

def plus(x, y):
    answer = x + y
    return answer # returnで戻り値を設定

answer = plus(100, 50)
print(f'足し算の答えは{answer}です。')

def input_scores(name):
    print(f'{name}さんの試験結果を入力してください。')
    network = int(input('ネットワークの得点?>>'))
    database = int(input('データベースの得点?>>'))
    security = int(input('セキュリティの得点?>>'))
    scores = [network, database, security] # inputの結果の変数をscores変数に格納
    return scores

def calc_average(scores):
    avg = sum(scores) / len(scores)
    return avg

def output_result(name, avg):
    print(f'{name}さんの平均点は{avg}点です。')

# 浅木と松田の得点を入力
asagi_scores = input_scores('浅木') # input_scores関数のリストが入る
matsuda_scores = input_scores('松田')

# 平均点を計算
asagi_avg = calc_average(asagi_scores) # 平均点を求めた後calc_average関数の戻り値が入る
matsuda_avg = calc_average(matsuda_scores)

#結果を出力
output_result('浅木', asagi_avg)
output_result('松田', matsuda_avg)


