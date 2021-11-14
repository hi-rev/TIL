n = int(input())
a = (n//10) + (n%10)
b = (n%10)
i = 0

while True:
    x = a % 10
    a = b + x
    i += 1
    if b == n//10 and x == n%10:
        break
    b = x
print(i)
