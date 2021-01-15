h, b, c, s = list(map(int, input().split(" ")))


space = h * b * c * s

print("{:.1f} MB".format(space / (1024 * 1024 * 8)))
