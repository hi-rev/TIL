n = int(input())
count = 0

def deduplication(w): # 연속된 중복 제거 함수
    result_list = []
    for i in range(len(w)):
        if i == 0:
            result_list.append(w[i])
        elif result_list[-1] != w[i]: # [-1]은 리스트의 마지막 요소
            result_list.append(w[i])
    return result_list

for i in range(n):
    s = input()
    word = deduplication([i for i in s]) # 중복제거
    cnt = [word.count(f'{i}') for i in word]

    if (sum(cnt) / len(cnt)) == 1:
        count += 1

print(count)
