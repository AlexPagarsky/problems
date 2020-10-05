class Solution:
    def sortColors(self, nums: List[int]) -> None:
        limit = len(nums)
        n = limit
        i = 0
        while i < n:
            Max, j = 0, 0
            while j < limit:
                if nums[j] > nums[Max]:
                    Max = j
                j += 1
            nums[limit-1], nums[Max] = nums[Max], nums[limit-1]
            limit -= 1
            i += 
        """
        Do not return anything, modify nums in-place instead.
        """
        