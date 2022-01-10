s = input()
cnt = 0
cnt_3 = 0

croatia = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia:
    if i in s:
        cnt += 1

    multi = int(s.count(i))
    if multi > 1:
        cnt += (multi-1)

if 'dz=' in s:
    cnt_3 += 1

multi = int(s.count('dz='))
if multi > 1:
    cnt_3 += (multi-1)

cnt = cnt - cnt_3

n = len(s) - 2*cnt - 3*cnt_3
print(n + cnt + cnt_3)
