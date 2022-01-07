word = input().lower() # 소문자 변환

from string import ascii_lowercase
alphabet_list = list(ascii_lowercase) # 알파벳 리스트

alphabet_count = [word.count(f'{i}') for i in alphabet_list]

pos = []
for i in range(len(alphabet_count)):
    if alphabet_count[i] == max(alphabet_count):
        pos.append(i)
# pos = [i for i in range(len(alphabet_count)) if alphabet_count[i] == cnt]

if len(pos) > 1:
    print('?')
else:
    indx = alphabet_count.index(max(alphabet_count))
    print(alphabet_list[indx].upper())
