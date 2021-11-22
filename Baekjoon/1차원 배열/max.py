nlist = []

for i in range(9):
    n = int(input())
    nlist.append(n)

print(max(nlist))
print(nlist.index(max(nlist))+1)
