file = open('text.txt', 'r').read()

dic = {}

for char in file:
  dic[char] = dic.get(char, 0) + 1

print ''.join(ch for ch in file if (dic[ch] == 1))
