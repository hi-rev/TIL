def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        ii = commands[i][0]
        j = commands[i][1]
        k = commands[i][2]

        new_array = array[ii-1:j]
        new_array.sort()
        answer.append(new_array[k-1])
    return answer
