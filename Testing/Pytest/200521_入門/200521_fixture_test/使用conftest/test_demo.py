import pytest


def test_one():
    print('這試測試用-1')


@pytest.mark.mytest
def test_two():
    print('這試測試用-2')


class TestCase:

    @pytest.mark.mytest
    def test_three(self):
        print('這試測試用-3')
