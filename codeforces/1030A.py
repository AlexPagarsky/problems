n = int(input())
res = sum(int(i) for i in input().split())
print('HARD') if res else print('EASY')