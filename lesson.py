num: int = 1
name: str = '1'
# 変数宣言に 変数名: データ型　とすることで
# 型指定が可能　だが、ほとんとのプログラムでは不要になっているため、必要なし

new_num = int(name)

print(new_num, type(new_num))

num = name

print(num, type(num))