n, h = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

width = 0

for i in range(len(a)):
    width = width+1 if a[i] <= h else width+2

print(width)