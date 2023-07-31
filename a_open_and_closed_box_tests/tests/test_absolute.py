from python.absolute import absolute_value_of

def test_1():
    assert absolute_value_of(1) == 1

def test_0():
    assert absolute_value_of(0) == 0

def test_negative_0():
    assert absolute_value_of(-0) == 0

def test_negative_1():
    assert absolute_value_of(-1) == 1

def test_negative_2():
    assert absolute_value_of(-2) == 2

# def test_nan():
#     assert absolute_value_of(float("nan")) == float("nan")

# def test_string():
#     assert absolute_value_of("test") == "test"

# def test_empty_string():
#     assert absolute_value_of("") == ""
