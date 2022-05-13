from blind_57.max_profit.index import Solution

solution = Solution()

def test_1_0():
    prices = [1, 2, 3]
    assert solution.maxProfit(prices) == 2


def test_1_1():
    prices = [1, 2, 3, 0]
    assert solution.maxProfit(prices) == 2


def test_1_2():
    prices = [1, 2, 3, 0, 1]
    assert solution.maxProfit(prices) == 2


def test_1_3():
    prices = [3, 2, 1]
    assert solution.maxProfit(prices) == 0


def test_1_4():
    prices = [3, 2, 1, 4]
    assert solution.maxProfit(prices) == 3