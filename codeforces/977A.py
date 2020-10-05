n, k = (int(i) for i in input().split())

while k:
    if n % 10:
        n -= 1
    else:
        n //= 10
    k -= 1

print(n)