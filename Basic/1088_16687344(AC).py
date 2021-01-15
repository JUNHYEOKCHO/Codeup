n = int(input())

list_num = []

[list_num.append(str(x)) for x in range(1, n+1) if x % 3 != 0]

print(" ".join(list_num))

