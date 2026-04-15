# モジュールについて
import math # mathモジュールの取り込みを宣言
import math as m # mathモジュールを別名で指定

print(f'円周率は{math.pi}です。') # mathモジュールにある変数pi　を参照
print(f'小数点以下を切り捨てれば{math.floor(math.pi)}です') # mathモジュールのfloor関数を呼び出す
print(f'小数点以下を切り上げれば{math.ceil(math.pi)}です') # mathモジュールのceil関数を呼び出す

# floor関数
# 整数以下の最大値の整数を返す

print(f'円周率は{m.pi}です')
print(f'小数点以下を切り捨てれば{m.floor(m.pi)}です')
print()
