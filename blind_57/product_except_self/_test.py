from blind_57.product_except_self.index import Solution

productExceptSelf = Solution().productExceptSelf

def test_product_except_self_0():
    assert type(productExceptSelf([1, 2])) is list, 'return value should be a list'


def test_product_except_self_1():
    result = productExceptSelf([1, 2])

    assert all([isinstance(num, int) for num in result]) == True, 'return value should be int list'


def test_product_except_self_1():
    assert productExceptSelf([1, 2]) == [2, 1]


def test_product_except_self_2():
    assert productExceptSelf([0, 1]) == [1, 0]


def test_product_except_self_3():
    assert productExceptSelf([0, 1, 2]) == [2, 0, 0]


def test_product_except_self_3():
    assert productExceptSelf([1, 2, 3]) == [6, 3, 2]
