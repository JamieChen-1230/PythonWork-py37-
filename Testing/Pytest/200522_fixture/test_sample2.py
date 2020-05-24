import pytest


@pytest.fixture()
def some_data():
    print("setup")      # yield前相當於執行setup
    yield 42            # yield跟return一樣也可以傳值
    print("teardown")   # yield後相當於執行teardown


def test_some_data(some_data):
    print('some_data:', some_data)
    assert some_data == 42
