h, w = list(map(int, input().split(" ")))

n = int(input())

map_ = []


for i in range(h):
    map_.append(['0'] * w)

for i in range(n):
    l, d, x, y = list(map(int, input().split(" ")))

    if d == 0:
        for j in range(l):
            if map_[x-1][y+j-1] == '1':
                continue
            else:
                map_[x-1][y+j-1] = '1'
    else:
        for j in range(l):
            if map_[x+j-1][y-1] == '1':
                continue
            else:
                map_[x+j-1][y-1] = '1'
                

for i in range(len(map_)):
    print(" ".join(map_[i]))
