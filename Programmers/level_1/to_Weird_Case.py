def solution(s):
    answer = []
    words = s.split(" ") # word List
    for i in words:
        word = list(i)
        for j in range(len(i)):
            if j % 2 == 0:
                word[j] = word[j].upper()
            else:
                word[j] = word[j].lower()
        join_word = "".join(word)
        answer.append(join_word)
        print(answer)
    return " ".join(answer) # 공백 포함!

# 문제에서는 '공백'을 기준으로 단어를 구분하라 하였다.
# split()을 사용하면 공백, 탭등과 같은 구분자가 모두 인식되므로
# 공백만을 구분자로 사용하려면 split(" ")을 사용해주어야 한다.
