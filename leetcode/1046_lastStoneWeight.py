from bisect import insort

class Solution:

    def smash(self, x : int, y : int):
        return 0 if x == y else abs(y-x)

    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            x = stones[-1]
            y = stones[-2]
            stones.pop(); stones.pop();
            insort(stones, self.smash(x, y))

        return stones[0]
