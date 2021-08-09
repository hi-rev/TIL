a = int(input())
b = int(input())
print(b % 10 * a, b % 100 // 10 * a, b // 100 * a, b * a)

"""
a = int(input())
b = int(input())

num1 = b // 100
num2 = (b - (num1*100)) // 10
num3 = b % 10

result1 = a * num3
result2 = a * num2
result3 = a * num1

sum = result1 + result2 * 10 + result3 * 100

print(result1)
print(result2)
print(result3)
print(sum)
"""
