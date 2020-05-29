import unittest


# 測試用例類(必須繼承Unuttest TestCase類)
class MyTestCase(unittest.TestCase):

    def test_1(self):
        print(1)

    def test_3(self):
        print(3)

    def test_2(self):
        print(2)

    def test_4(self):
        print(4)

    def test_5(self):
        print(5)


if __name__ == '__main__':
    unittest.main()
