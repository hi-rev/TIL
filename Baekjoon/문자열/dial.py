s = input()

s_list = [i for i in s] # 알파벳 리스트

for i in s_list:
    indx = s_list.index(i)
    if i == 'A' or i == 'B' or i == 'C':
        s_list[indx] = 2;
    elif i == 'D' or i == 'E' or i == 'F':
        s_list[indx] = 3;
    elif i == 'G' or i == 'H' or i == 'I':
        s_list[indx] = 4;
    elif i == 'J' or i == 'K' or i == 'L':
        s_list[indx] = 5;
    elif i == 'M' or i == 'N' or i == 'O':
        s_list[indx] = 6;
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        s_list[indx] = 7;
    elif i == 'T' or i == 'U' or i == 'V':
        s_list[indx] = 8;
    elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        s_list[indx] = 9;

print(sum(s_list) + len(s_list))
