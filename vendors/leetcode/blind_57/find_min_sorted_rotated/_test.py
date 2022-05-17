from blind_57.find_min_sorted_rotated.index import Solution

findMin = Solution().findMin


def test_find_min_sorted_rotated_1():
    nums = [3, 4, 5, 6, 1, 2]

    assert findMin(nums) == 1


def test_find_min_sorted_rotated_2():
    nums = [7, 8, 2, 3, 4, 5, 6]

    assert findMin(nums) == 2


def test_find_min_sorted_rotated_3():
    nums = [-100, -99, -103, -102, -101]

    assert findMin(nums) == -103
