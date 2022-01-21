dot_x = []
dot_y = []

for i in range(3):
    x, y = map(int, input().split())
    dot_x.append(x)
    dot_y.append(y)

for i in range(3):
    if dot_x.count(dot_x[i]) == 1:
        print(dot_x[i], end=" ")

for i in range(3):
    if dot_y.count(dot_y[i]) == 1:
        print(dot_y[i])
