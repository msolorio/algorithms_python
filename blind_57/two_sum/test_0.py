from blind_57.two_sum.index import two_sum


def test_0_0():
    assert two_sum([1, 2, 3], 5) == [1, 2]

def test_0_1():
    assert two_sum([1, 2], 5) == None

def test_0_2():
    assert two_sum([1], 5) == None

def test_0_3():
    assert two_sum([], 5) == None

def test_0_4():
    assert two_sum([0, 0], 0) == [0, 1]

def test_0_5():
    assert two_sum([3, 2, 1], 3) == [1, 2]

def test_0_5():
    assert two_sum([3, 2, 1], 4) == [0, 2]