n = int(input())

num_list = []

for i in range(1, 6):
    num = n % (10 ** i)
    num_list.append(num)
    n -= num
    
num_list.reverse()

for x in num_list:
    print("[%d]" %x)
