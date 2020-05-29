import unittest


# 測試用例類(必須繼承Unuttest TestCase類)
class MyTestCase(unittest.TestCase):
    # 用例類前置條件
    @classmethod
    def setUpClass(cls) -> None:
        print('類級別的setup')

    # 用例類後置條件
    @classmethod
    def tearDownClass(cls) -> None:
        print('類級別的teardown')

    # 用例前置條件
    def setUp(self) -> None:
        print('方法級別的setup')

    # 用例後置條件
    def tearDown(self) -> None:
        print('方法級別的teardown')

    # 測試用例
    # 名稱定義： def test_*() 或 def *_test()
    def test_a(self):
        print('a')

    def test_b(self):
        print('b')


if __name__ == '__main__':
    unittest.main()
