def solution(s, n):
    answer = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in s:
        if i.isupper(): # 대문자일 때 변환
            answer.append(alphabet_up[(alphabet_up.index(i) + n) % 26])
        elif i == " ": # 공백일 때
            answer.append(" ")
        else: # 소문자일 때 변환
            answer.append(alphabet[(alphabet.index(i) + n) % 26])

    return "".join(answer)
