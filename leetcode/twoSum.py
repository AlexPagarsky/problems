class Solution:
    def twoSum(self, nums, target):
        checked = {}
        for i in range(0, len(nums)):
            d = target - nums[i]
            if d in checked:
                return [checked[d], i]
            checked[nums[i]] = i

sol = Solution()

# print(list(enumerate([3, 2, 4])))
print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum([3, 2, 4], 6))
print(sol.twoSum([3, 3], 6))