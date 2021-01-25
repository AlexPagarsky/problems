class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return True

        counter = k

        for n in nums:
            if n == 0:
                counter += 1
            else: # n == 1
                if counter < k:
                    return False
                counter = 0

        return True