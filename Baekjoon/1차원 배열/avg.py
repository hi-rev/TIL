n = int(input())

test_list = list(map(int, input().split())) # 점수 list
m = max(test_list) # 가장 높은 점수

new_test_list = []

for i in range(n):
    a = test_list[i] / m*100
    new_test_list.append(a)

print(sum(new_test_list) / n)
