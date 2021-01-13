a = int(input())

num = []

[num.append(str(x)) for x in range(a)]

num.reverse()

print("\n".join(num))
