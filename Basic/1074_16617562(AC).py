a = int(input())

num = []

[num.append(str(x)) for x in range(1, a+1)]

num.reverse()

print("\n".join(num))

