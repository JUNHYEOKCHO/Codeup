a = input()

hexnum = int(a, 16)

for i in range(1, 16):
    print("%s*%X=%X" %(a, i, hexnum * i))
