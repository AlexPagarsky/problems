class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        res = nums[0]

        for i in nums[1:]:
            res ^= i

        return res