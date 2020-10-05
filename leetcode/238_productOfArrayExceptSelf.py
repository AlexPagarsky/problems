class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        output = [1] * l

        i, j = 0, l
        L, R = 1, 1

        while j:
            output[i] *= L
            output[j-1] *= R
            L *= nums[i]
            R *= nums[j-1]
            i += 1
            j -= 1


        return output