from typing import List
########################################################
# Without using set()
# O(n)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) <= 1:
            return False

        cache = {}

        for num in nums:
            if num in cache:
                return True
        
            else:
                cache[num] = 1

        return False


########################################################
# Using python set() - too easy ########################
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         original_length = len(nums)

#         unique_length = len(set(nums))

#         return original_length != unique_length


