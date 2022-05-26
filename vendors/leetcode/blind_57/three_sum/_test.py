from blind_57.three_sum.index import Solution

threeSum = Solution().threeSum

def test_three_sum_0():
    nums = [0, 0, 0]

    assert threeSum(nums) == {(0, 0, 0)}


def test_three_sum_0():
    nums = [0, 0, 0, 0]

    assert threeSum(nums) == {(0, 0, 0)}


def test_three_sum_0():
    nums = [1, 0, -1]

    assert threeSum(nums) == {(-1, 0, 1)}
    
    
def test_three_sum_0():
    nums = [1, 0, -1, -1]

    assert threeSum(nums) == {(-1, 0, 1)}


def test_three_sum_0():
    nums = [1, 0, -2]

    assert threeSum(nums) == set()

    
def test_three_sum_0():
    nums = [1, 0, -1, -1]

    assert threeSum(nums) == {(-1, 0, 1)}
    
    
def test_three_sum_0():
    nums = [-1, 2, -1]

    assert threeSum(nums) == {(-1, -1, 2)}


def test_three_sum_0():
    nums = [1, -2, 1]

    assert threeSum(nums) == {(-2, 1, 1)}
    

def test_three_sum_0():
    nums = [-1, -2, -1]

    assert threeSum(nums) == set()
    
    
def test_three_sum_0():
    nums = [1, 2, 1]

    assert threeSum(nums) == set()
    

def test_three_sum_0():
    nums = [1, -1]

    assert threeSum(nums) == set()
    

def test_three_sum_0():
    nums = [1]

    assert threeSum(nums) == set()
    

def test_three_sum_0():
    nums = []

    assert threeSum(nums) == set()