class Solution:
    def climbStairs(self, n: int) -> int:
        
        def fib(n : int) -> int:
            a = 1
            b = 1

            for i in range(1, n):
                temp = a
                a += b
                b = temp
            return a

        return fib(n)




sol = Solution()

print(sol.climbStairs(int(input())))