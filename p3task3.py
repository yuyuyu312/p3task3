list = []
n = int(input())
for i in range(n):
    k = int(input())
    list.append(k)

a = int(input("input yor num"))
if a < 0:
    list.reverse()
for i in range(abs(a)):
    list.append(list[i])
    del(list[i])
if a < 0:
    list.reverse()
print(list)
