def cal(a, m, d):
    return a*m + d

a, m, d, n = list(map(int, input().split(" ")))

for i in range(n-1):
    a = cal(a, m, d)
print(a)
