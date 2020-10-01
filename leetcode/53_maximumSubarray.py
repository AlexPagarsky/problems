class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = temp = nums[0]
        
        for i in range(1, len(nums)):
            temp = max(temp + nums[i], nums[i])
            m = max(m, temp)
        return m