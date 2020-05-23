import pytest


def setup_module():
    print('模塊級別的setup')


def teardown_module():
    print('模塊級別的teardown')


def setup_function():
    print('函數級別的setup')


def teardown_function():
    print('函數級別的teardown')


def test_one():
    print('這試測試用-1')


# 類名為Test*
class TestCase:
    def setup_class(self):
        print('類級別的setup')

    def teardown_class(self):
        print('類級別的teardown')

    def setup_method(self):
        print('方法級別的setup')

    def teardown_method(self):
        print('方法級別的teardown')

    def setup(self):
        print('普通的setup')

    def teardown(self):
        print('普通的teardown')

    # 方法名為test_*
    def test_two(self):
        print('這試測試用-2')

    def test_three(self):
        print('這試測試用-3')


if __name__ == '__main__':
    pytest.main('-v', '-s')
