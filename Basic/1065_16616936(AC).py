a = list(map(int,input().split(" ")))

even = list()

[even.append(str(x)) for x in a if x % 2 == 0]


print("\n".join(even))

