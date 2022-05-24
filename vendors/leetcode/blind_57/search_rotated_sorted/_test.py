from blind_57.search_rotated_sorted.index import Solution

search = Solution().search

def test_find_min_sorted_rotated_0():
    nums = [3, 4, 5, 6, 1, 2]

    assert search(nums, 3) == 0

def test_find_min_sorted_rotated_1():
    nums = [3, 4, 5, 6, 1, 2]

    assert search(nums, 4) == 1

def test_find_min_sorted_rotated_2():
    nums = [3, 4, 5, 6, 1, 2]

    assert search(nums, 5) == 2

def test_find_min_sorted_rotated_3():
    nums = [3, 4, 5, 6, 1, 2]

    assert search(nums, 6) == 3

def test_find_min_sorted_rotated_4():
    nums = [3, 4, 5, 6, 1, 2]

    assert search(nums, 1) == 4

def test_find_min_sorted_rotated_5():
    nums = [3, 4, 5, 6, 1, 2]

    assert search(nums, 2) == 5
