class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        nth_bit = 1 << n
        for i in range(2**n):
            mask, sub = bin(i | nth_bit)[3:], []
            for j in range(n):
                if mask[j] == '1': sub.append(nums[j])
            res.append(sub)
        return res