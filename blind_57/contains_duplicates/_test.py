from blind_57.contains_duplicates.index import Solution

containsDuplicate = Solution().containsDuplicate

def test_contains_duplicates_0():
    assert type(containsDuplicate([1, 2])) is bool


def test_contains_duplicates_1():
    assert containsDuplicate([1, 2]) == False


def test_contains_duplicates_2():
    assert containsDuplicate([1, 1]) == True


def test_contains_duplicates_3():
    assert containsDuplicate([0, 1, 2, 3, 0]) == True


def test_contains_duplicates_4():
    assert containsDuplicate([0, 1, 2, 3, 4]) == False


def test_contains_duplicates_4():
    assert containsDuplicate([-1, 1]) == False
