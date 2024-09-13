import pytest
@pytest.fixture()
def before_after_test():
    print("\nbefore executing tests")
    yield
    print("\nafter executing test")

def test_1():
    assert 1 == 1

def test_random_method(before_after_test):
    assert 2 == 2