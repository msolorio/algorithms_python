from typing import List

class Solution:
    # triple nested loop - After looking at LeetCode solutions
    # O(n^2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = set()

        # sort numbers into positives, negatives, and zeros
        positives, negatives, zeros = [], [], []

        for num in nums:
            if num < 0:
                negatives.append(num)
            elif num > 0:
                positives.append(num)
            else:
                zeros.append(nums)


        # If zero in the list, see if negative and positive opposites exist (-1, 1)
        if len(zeros):
            for num in positives:
                neg_num = -1 * num

                if (neg_num) in negatives:
                    solution.add((neg_num, 0, num))

        # for all negative pairs see if positive complement exists (-1, -1, 2)
        for i in range(len(negatives)):
            for j in range(i + 1, len(negatives)):
                comp = -1 * (negatives[i] + negatives[j])
                if comp in positives:
                    sol = tuple(sorted((negatives[i], negatives[j], comp)))
                    
                    solution.add(sol)

        # for all positive pairs see if negative complement exists
        for i in range(len(positives)):
            for j in range(i + 1, len(positives)):
                comp = -1 * (positives[i] + positives[j])
                if comp in negatives:
                    sol = tuple(sorted((positives[i], positives[j], comp)))
                    
                    
                    solution.add(sol)

        # check if 3 zeros exist
        if len(zeros) >= 3:
            solution.add((0, 0, 0))

        return solution

combos = Solution().threeSum([1, 0 -2])

print(combos)
