def test():
    n = int(input())
    res = 0
    cost = {
    'Tetrahedron' : 4,
    'Cube' : 6,
    'Octahedron' : 8,
    'Dodecahedron' : 12,
    'Icosahedron' : 20
    }

    while n:
        s = input()
        res += cost[s]
        n -= 1
    print(res)

test()