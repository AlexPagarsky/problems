def f(n):
    s = 0
    for k in range(1, n+1):
        s += (-1)**k * k
    return s

print(f(int(input())))