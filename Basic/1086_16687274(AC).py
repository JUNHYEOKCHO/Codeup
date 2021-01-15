w, h, b = list(map(int, input().split(" ")))


space = w * h * b

print("{:.2f} MB".format(space / (1024 * 1024 * 8)))

