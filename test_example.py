def sum(a, b):
    return a + b

def test_sum_success():
    assert sum(1, 2) == 3

def test_sum_fail():
    assert sum(1, 2) == 4
