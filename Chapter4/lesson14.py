# 組み込み関数について
# print 引数を標準出力に出力する
# input　　標準入力から一行読み込んだ結果を返す

# open関数について　引数１　開くファイルの名前、引数２　モードを指定
text = input('何を記録しますか？>>')
file = open('diary.txt', 'a') # ファイルを開く 'a'は追記モード
file.write(text + '\n') # text と改行
file.close() # ファイルを閉じる

# with文 usingと同じようにclose()
# with ファイルを開く処理 as 変数:
#   ファイルを操作する処理
text = input('今日は何をした？>>')
with open('diary1.txt', 'a') as file:
    file.write(text + '\n')

