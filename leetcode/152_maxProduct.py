class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = lmax = lmin = temp = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                lmax, lmin = lmin, lmax

            lmax = max(lmax * nums[i], nums[i])
            lmin = min(lmin * nums[i], nums[i])

            m = max(lmax, m)

        return m