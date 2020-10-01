def test():
    n = int(input())

    out = ['I', 'hate', 'it']

    if n == 1: print('I hate it'); return
    n -= 1

    while n:
        out.insert(2, 'that I love' if n % 2 else 'that I hate')
        n -= 1
    print(' '.join(out))


test()