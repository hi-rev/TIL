a, b = input().split()

aa = [i for i in a]
bb = [i for i in b]
aa.reverse()
bb.reverse()

num = [int(''.join(aa)), int(''.join(bb))]
print(max(num))
