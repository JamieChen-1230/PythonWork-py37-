import pytest


@pytest.fixture()  # 默認為function級別
def rung_func_username():
    print("\n獲取用戶名：")
    name = 'jamie'
    return name


@pytest.fixture(scope="function")  # function級別的表示每次執行方法都會執行一次
def rung_func_password():
    print("\n獲取密碼：")
    pwd = '123'
    return pwd


@pytest.fixture(scope="class")  # class級別的表示只會在執行測試類的時候最多執行一次(不管裡面有幾個方法調用它)
def rung_class():
    print("\n我是class等級的")


@pytest.fixture(scope="module")  # module級別的表示在執行本模塊中最多執行一次(不管裡面有幾個方法調用它)
def rung_module():
    print("\n我是module等級的")


def test_0(rung_module):
    print('此為test0')


def test_1(rung_func_username, rung_func_password):
    print('用戶名為', rung_func_username)
    print('密碼為', rung_func_password)
    assert rung_func_username == 'jamie' and rung_func_password == '123'


class TestCase:

    def test_2(self, rung_func_username, rung_func_password, rung_class, rung_module):
        print('用戶名為', rung_func_username)
        print('密碼為', rung_func_password)

    def test_3(self, rung_class):
        print('此為test3')

