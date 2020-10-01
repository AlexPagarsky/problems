from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache()
        def call(m, n):
            if m == 0 and n == 0: return 1
            if m-1 >= 0 and n-1 >= 0:
                p = call(m-1, n) + call(m, n-1)
            elif m-1 >= 0:
                p = call(m-1, n)
            elif n-1 >= 0:
                p = call(m, n-1)
            return p or 1

        return call(m-1, n-1)