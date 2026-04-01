print('print')
print("hello")
print("I don't know")
print('say "I dont\'t know"')

print('hello. \nHow are you?')
print(r'C:\name\name')

print("########")
print("""
line1
line2
line3\
""")
print("#########")

print('Hi.' * 3 + 'Mike')
print('Py' + 'thon')

prefix = 'Py'
print(prefix + 'thon')

# インデックスで表示
word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print(word[2:]) # 2番目から最後まで
word[0] = 'j' + word[1:]
print(word)
