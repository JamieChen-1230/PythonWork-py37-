import pytest


# autouse=True 代表全部測試方法都會調用他
@pytest.fixture(scope="function", autouse=True)
def all_fun():
    print("全部都有我")


# 被@pytest.fixture()裝飾的函數可以當作test方法的變量
@pytest.fixture(scope="package")
def login():
    print('這是一個登入方法')


# params為參數，被裝飾的函數要接收必須透過request才能調用
@pytest.fixture(scope="function", params=[1, 2, 5])
def date(request):  # 至少要有一個request參數
    print('這是一個date方法')
    return request.param  # 獲取參數


# 變量login對應著login函數
# 在測試前會先運行login函數
def test_one(login):
    print('這試測試用-1')


def test_three(date):
    print('這試測試用-3   -->  ', date)


class TestCase:
    # 方法名為test_*
    def test_two(self, login):
        print('這試測試用-2')


