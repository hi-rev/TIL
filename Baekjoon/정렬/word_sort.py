# 단어 갯수
n = int(input())

word = [input() for i in range(n)]

set_word = list(set(word))
set_word.sort()
set_word.sort(key = lambda x : len(x))

for i in set_word:
    print(i)
