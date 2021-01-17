import collections 

n = int(input())
a = list(map(str, input().split(" ")))

b = collections.Counter(a)

num_list = []

for i in range(1, 24):
    if str(i) in b.keys():
        num_list.append(str(b[str(i)]))
    else:
        num_list.append("0")

print(" ".join(num_list))
