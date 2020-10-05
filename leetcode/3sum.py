from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        nums.sort()
        length = len(nums)
        
        for i in range(length-2):
            
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue

            left, right = i+1, length-1

            while left < right:
                res = nums[i] + nums[left] + nums[right]

                if res < 0:
                    left += 1
                elif res > 0:
                    right -= 1
                else:
                    solutions.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]: left += 1
                    while left < right and nums[right] == nums[right-1]: right -= 1

                left += 1
                right -= 1

        return solutions