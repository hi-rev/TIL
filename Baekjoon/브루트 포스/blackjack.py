# 블랙잭
# 1. 3장의 카드 고르기
# 2. 카드의 합은 M을 넘지 않으면서 M과 가깝게 만들기
# 3. 제시된 카드 중 위 조건에 맞는 카드 3개의 합

n, m = map(int, input().split())
card = list(map(int, input().split())) # card 중 3개의 요소의 모든 합
answer = []

for i in range(len(card) - 2):
    for j in range(i+1, len(card) - 1):
        for l in range(j+1, len(card)):
            cardSum = card[i]+card[j]+card[l]
            if cardSum <= m:
                answer.append(cardSum)

print(max(answer))
