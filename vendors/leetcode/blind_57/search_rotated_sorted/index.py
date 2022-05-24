"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1

Constraints:

    1 <= nums.length <= 5000
    -104 <= nums[i] <= 104
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
    -104 <= target <= 104
"""

from typing import List

###########################################################
# Solution after looking at LeetCode solutions
# O(log n)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        str = 0
        end = len(nums) - 1

        while str <= end:
            mid = (str + end) // 2

            if nums[mid] == target:
                return mid
            
            if nums[str] <= nums[mid]:
                if nums[str] <= target < nums[mid]:
                    end = mid - 1
                else:
                    str = mid + 1

            else:
                if nums[mid] < target <= nums[end]:
                    str = mid + 1
                else:
                    end = mid - 1

        return str
            

print(Solution().search([3, 4, 5, 6, 1, 2], 2))


# Not working solution
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         start_idx = 0
#         end_idx = len(nums) - 1

#         while end_idx > start_idx:
#             mid_idx = (start_idx + end_idx) // 2

#             if target == nums[mid_idx]:
#                 return mid_idx

#             start_num = nums[start_idx]
#             end_num = nums[end_idx]
#             mid_num = nums[mid_idx]

#             print (start_idx, mid_idx, end_idx)

#             if (
#                 (mid_num < end_num and target <= mid_num) or 
#                 (target >= start_num and target <= mid_num)
#             ):
#                 end_idx = mid_idx - 1
#             else:
#                 start_idx = mid_idx

#         if nums[start_idx] == target:
#             return start_idx
#         else:
#             return -1

# search = Solution().search

# print('result:', search([3, 4, 5, 6, 1, 2], 3))
# print('result:', search([4,5,6,7,0,1,2], 3))
