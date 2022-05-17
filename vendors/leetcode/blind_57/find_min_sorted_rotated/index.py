"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

Constraints:

    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    All the integers of nums are unique.
    nums is sorted and rotated between 1 and n times.

"""
import math
from typing import List

##################################################################
# My solution using recursion
# O(log n)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return min(nums)

        mid_idx = math.ceil(len(nums)/2)

        first_half = nums[:mid_idx]
        second_half = nums[mid_idx:]
        second_min = min(second_half[0], second_half[-1])
        first_min = min(first_half[0], first_half[-1])

        if first_min < second_min:
            return self.findMin(first_half)

        else:
            return self.findMin(second_half)


##################################################################
# After looking at LeetCode solutions
# O(log n)
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         if len(nums) <= 2:
#             return min(nums)

#         mid_idx = len(nums) // 2 

#         if nums[mid_idx] < nums[0]:
#             first_half = nums[:mid_idx]
#             return self.findMin(first_half)

#         else:
#             second_half = nums[mid_idx:]
#             return self.findMin(second_half)

##################################################################
# After looking at LeetCode solutions
# O(log n)
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         start = 0
#         end = len(nums) - 1

#         while start < end:
#             mid = (start + end) // 2

#             if nums[mid] > nums[end]:
#                 start = mid + 1

#             else:
#                 end = mid

#         return nums[start]


##################################################################
# Brute force
# O(n) - we can do better
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         min = float('inf')

#         for num in nums:
#             if num < min:
#                 min = num

#         return min

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         return min(nums)