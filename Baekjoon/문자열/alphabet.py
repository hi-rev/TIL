from string import ascii_lowercase

alphabet_list = list(ascii_lowercase) # 알파벳 리스트
s = input()

for i in alphabet_list:
    print(s.find('{0}'.format(i)), end=' ')
