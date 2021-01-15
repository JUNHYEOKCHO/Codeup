a = list(map(int, input().split(" ")))

num = 0 

for r in range(a[0]):
    for g in range(a[1]):
        for b in range(a[2]):
            print("%d %d %d" %(r, g, b))

            num += 1

print(num)
