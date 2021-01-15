n = int(input())

num_list = []

for x in range(1, n+1):
    if x % 3 == 0:
        num_list.append("X")
    else:
        num_list.append(str(x))

print(" ".join(num_list))
