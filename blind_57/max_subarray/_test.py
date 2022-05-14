from blind_57.max_subarray.index import Solution

maxSubArray = Solution().maxSubArray

def test_max_subarray_0():
    nums = [1, 2, -10, 3, 5]

    assert maxSubArray(nums) == 8

def test_max_subarray_1():
    nums = [1, 2, -2, 3, 5]

    assert maxSubArray(nums) == 9


def test_max_subarray_2():
    nums = [-5, -3, -1, -4]

    assert maxSubArray(nums) == -1


def test_max_subarray_2():
    nums = [-1, -5, -3, -4]

    assert maxSubArray(nums) == -1



def test_max_subarray_2():
    nums = [-1, -5, -3, 0, -4]

    assert maxSubArray(nums) == 0


def test_max_subarray_2():
    nums = [-3, 5, -4, 23]

    assert maxSubArray(nums) == 24