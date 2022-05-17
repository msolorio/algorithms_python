"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

from typing import List

################################################################
# Solution using division operator
# O(n)
# class Solution:
#     def getTotalProduct(self, nums: List[int]) -> int:
#         product = 1

#         for num in nums:
#             product = product * num

#         return product

#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         total_product = self.getTotalProduct(nums)
#         products = [total_product] * len(nums)

#         for idx, product in enumerate(products):
#             if nums[idx] == 0:
#                 filtered = [num for num in nums if num != 0]
#                 product = self.getTotalProduct(filtered)
#                 products[idx] = product

#             else:
#                 products[idx] = products[idx] / nums[idx]

#         return products

###############################################################
# Solution from others at leetCode - no division operator
# O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> int:
        nums_len = len(nums)
        products = [1] * nums_len

        # multiply nums from left to right
        pre = 1
        for i in range(nums_len):
            products[i] *= pre
            pre = nums[i]

        # multiply nums from right to left
        post = 1
        for i in range(nums_len - 1, -1, -1):
            products[i] *= post
            post *= nums[i]
        
        return products


"""
Explanation

nums = [2, 5, 1, 7]

                                [1, 1, 1 ,1]
multiply from left to right         2  2  2
                                       5  5
                                          1
multiply from right to left     7   7  7   
                                1   1
                                5

Each index gets multiplied by every number except itself

"""