def plus_and_minus(a, b):
    return(a + b, a- b) # 要素二つのタプルを返している。returnで整数二つを返すことはない。

(next, prev) = plus_and_minus(1978, 1) # タプルで戻ってきた値がアンパック代入(2つ以上の定義)している。