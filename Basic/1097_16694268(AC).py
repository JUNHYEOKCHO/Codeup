list_ = []

for _ in range(19):
    a = list(map(int, input().strip().split(" ")))

    list_.append(a)


n = int(input())


for i in range(n):
    a, b = list(map(int, input().strip().split(" ")))

    for i in range(19):
        if list_[a-1][i] == 0:
            list_[a-1][i] = 1
        else:
            list_[a-1][i] = 0
    for i in range(19):
        if list_[i][b-1] == 0:
            list_[i][b-1] = 1
        else:
            list_[i][b-1] = 0
            

for i in range(19):
    line = ""
    for j in range(19):
        k = str(list_[i][j])
        line += k + " "

    print(line)
