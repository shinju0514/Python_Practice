
# elseブロックがない分岐
name = input('あなたの名前を教えてください。>>')
print(f'{name}さんこんにちは')
if name == '松田':
    print('松田さんに会えて嬉しいです。')
food = input(f'{name}さんの好きな食べ物を教えてください。>>')
if 'カレー' in food: # foodの中に'カレー'が含まれていればTrue
    print('カレーはうまいですよね')
else:
    print(f'私も{food}が好きですよ')

