class Solution:
    def searchInsert(self, nums, target: int) -> int:
        lo = 0
        hi = len(nums)-1
        index = -1

        while lo <= hi:
            index = (lo+hi) // 2

            if target < nums[index]:
                index = hi
            else:
                index = lo

        return index if target < nums[index] else index + 1



sol = Solution()
l = [1, 3, 5, 6]
target = 0
print(l, target)
print(sol.searchInsert(l, target))



# ##########
# class Solution:
#     def searchInsert(self, nums, target: int) -> int:
#         index = 0
#         hi = len(nums) - 1
#         lo = 0
#         if target > nums[hi]:
#             return hi+1
#         elif target < nums[0]:
#             return 0

#         while target != nums[index]:
#             index = (hi+lo) // 2
#             if target > nums[index]:
#                 lo = index
#             else:
#                 hi = index

#             if hi == lo+1:
#                 return hi
#         return index