from blind_57.two_sum.index import two_sum


def test_two_sum_0():
    assert two_sum([1, 2, 3], 5) == [1, 2]

def test_two_sum_1():
    assert two_sum([1, 2], 5) == None

def test_two_sum_2():
    assert two_sum([1], 5) == None

def test_two_sum_3():
    assert two_sum([], 5) == None

def test_two_sum_4():
    assert two_sum([0, 0], 0) == [0, 1]

def test_two_sum_5():
    assert two_sum([3, 2, 1], 3) == [1, 2]

def test_two_sum_5():
    assert two_sum([3, 2, 1], 4) == [0, 2]