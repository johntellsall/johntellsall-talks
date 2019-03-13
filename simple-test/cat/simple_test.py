def divide(a, b):
    return a / b

def test_happy():
    assert divide(5, 2) == 2.5

def test_happy_verbose():
    result = divide(5, 2)
    assert result == 2.5