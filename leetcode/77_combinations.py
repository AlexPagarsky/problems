class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not n: return []
        if n == 1: return [[1]]
        if k == 1: return [[x] for x in range(1, n+1)]
        
        def call(nums, i):
            if len(nums) <= k:
                nums.append(i)
                call(nums, i+1)

        res = []

        for i in range(n):
            res.append()


        return res