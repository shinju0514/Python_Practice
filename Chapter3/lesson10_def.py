def plus_and_minus(a, b):
    return(a + b, a- b) # 要素二つのタプルを返している。returnで整数二つを返すことはない。

(next, prev) = plus_and_minus(1978, 1) # タプルで戻ってきた値がアンパック代入(2つ以上の定義)している。

# def 関数名(仮引数名 = デフォルト値,・・・):
# 処理
# return 戻り値

def eat(breakfast, lunch='ラーメン', dinner='カレー'): # 仮引数 = デフォルト値 でデフォルト値を設定
    print(f'朝は{breakfast}を食べました。')
    print(f'昼は{lunch}を食べました。')
    print(f'夜は{dinner}を食べました。')

print('8月1日')
eat('トースト', 'おにぎり')
print('8月2日')
eat('納豆ごはん', 'ラーメン')
print('8月3日')
eat('バナナ', 'そば')
print('8月4日')
eat('サンドウィッチ', 'シュウマイ弁当')

# def eat(breakfast='パン', lunch, dinner='カレー'): # とするとエラーになる
# デフォルト引数を利用する際は、必ず一番後ろの引数から使用しないといけない

# 引数にキーワードを指定した関数呼び出し
# 関数名(仮引数名1=実引数1, 仮引数名2=実引数2, ・・・)

eat(breakfast='納豆ごはん', dinner='カレーうどん')
eat(dinner='カレーうどん', breakfast='納豆ごはん')
eat('納豆ごはん', dinner='カレーうどん')

# 可変超引数について 呼び出し時にn個以上の実引数を指定できる
# def 関数名(仮引数1, 仮引数2, ・・・, *仮引数名n):
def eat(breakfast, lunch, dinner='カレー', *desserts): # dessertsは可変長引数を表明
    print(f'朝は{breakfast}を食べました。')
    print(f'昼は{lunch}を食べました。')
    print(f'晩は{dinner}を食べました。')
    for d in desserts:
        print(f'おやつに{d}を食べました。')
eat('トースト', 'パスタ', 'カレー', 'アイス', 'チョコ', 'ポテチ') # 最後のアイス、チョコ、ポテチがタプル
