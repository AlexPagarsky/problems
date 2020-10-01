class Solution:
    def climbStairs(self, n: int) -> int:
        comp = [1, 1]
        for i in range(2, n):
            comp.append(comp[i-1]+comp[i-2])
        return comp[n-1]
            

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         computed = {0:1, 1:1}
#         def fib(n: int) -> int:
#             if n in computed:
#                 return computed[n]
#             computed[n] = fib(n-2) + fib(n-1)
#             return computed[n]
        
#         return fib(n)