"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""

from typing import List

###################################################################
# Non-working but very close solution
# O(n)
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         possible_largests = [0]

#         for num in nums:
#             if num > 0:
#                 possible_largests[-1] += num

#             if num < 0:
#                 new_possible = possible_largests[-1] + num

#                 possible_largests.append(new_possible)

#         print('possible_largests:', possible_largests)

#         largest = float('-inf')

#         for num in possible_largests:
#             if num > largest:
#                 largest = num
        
#         return largest


###################################################################
# Solution after looking at leetCode solutions
# O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        largest = nums[0]

        for num in nums[1:]:
            if num > current + num:
                current = num
            else:
                current += num

            largest = max(current, largest)

        return largest
