from blind_57.max_profit.index import Solution

solution = Solution()

def test_max_profit_0():
    prices = [1, 2, 3]
    assert solution.maxProfit(prices) == 2


def test_max_profit_1():
    prices = [1, 2, 3, 0]
    assert solution.maxProfit(prices) == 2


def test_max_profit_2():
    prices = [1, 2, 3, 0, 1]
    assert solution.maxProfit(prices) == 2


def test_max_profit_3():
    prices = [3, 2, 1]
    assert solution.maxProfit(prices) == 0


def test_max_profit_4():
    prices = [3, 2, 1, 4]
    assert solution.maxProfit(prices) == 3