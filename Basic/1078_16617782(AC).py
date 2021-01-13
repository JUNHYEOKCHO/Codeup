n = int(input())

sum_ = 0

for x in range(1, n+1):
    if x % 2 == 0:
        sum_ += x

print(sum_)
