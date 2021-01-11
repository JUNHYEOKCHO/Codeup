a = int(input())

output = []

if a < 0:
    output.append('minus')
else:
    output.append('plus')

if a % 2 == 0:
    output.append('even')
else:
    output.append("odd")

print("\n".join(output))

