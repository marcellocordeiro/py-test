def div(a, b):
    return a / b

def test_div_success():
    assert div(4, 2) == 2

def test_div_fail():
    assert div(4, 2) == 3
