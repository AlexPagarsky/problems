class Solution:
    def isHappy(self, n: int) -> bool:
        been = set()
        while n != 1:
            if n in been: return False
            been.add(n)
            n = (int(d) for d in str(n))
            n = sum((d**2 for d in n))
        return True



if __name__ == '__main__':
    n = int(input())
    sol = Solution()
    print(sol.isHappy(n))