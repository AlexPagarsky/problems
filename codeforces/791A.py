a, b = (int(i) for i in input().split())
i = 0

while a <= b:
    a *= 3
    b *= 2
    i += 1

print(i)