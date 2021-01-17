map_ = []

for i in range(10):
    line = list(map(str, input().split(" ")))

    map_.append(line)

x = 1
y = 1

while True:
    if map_[x][y] == '0':
        map_[x][y] = '9'
        continue
    elif map_[x][y] == '2':
        map_[x][y] = '9'
        break
    elif (map_[x][y+1] == '0') or map_[x][y+1] == '2': # 오른쪽이 0이면 우선 가게끔 만들기
        y += 1
        continue
    elif map_[x][y+1] != '0': # 오른쪽이 0이 아니다?
        if map_[x+1][y] == '0' or map_[x+1][y] == '2':
            x += 1
        else:
            break

for i in range(len(map_)):
    print(" ".join(map_[i]))
        

