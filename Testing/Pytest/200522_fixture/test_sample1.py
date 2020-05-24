import pytest


@pytest.fixture()
def some_data():
    return 42


def test_some_data(some_data):
    assert some_data == 42


@pytest.fixture()
def a_list():
    return [1, 2, 3, 9, 10]


def test_a_list(a_list):
    assert a_list[2] == 10
