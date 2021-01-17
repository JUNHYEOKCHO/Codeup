n = int(input())

list_ = []

for i in range(19):
    list_.append([0]*19)

for i in range(n):
    a, b = list(map(int, input().strip().split(" ")))
    list_[a-1][b-1] = 1

for i in range(19):
    line = ""
    for j in range(19):
        k = str(list_[i][j])
        line += k + " "

    print(line)
