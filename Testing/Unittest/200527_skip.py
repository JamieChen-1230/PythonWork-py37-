import unittest


# 測試用例類(必須繼承Unuttest TestCase類)
class MyTestCase(unittest.TestCase):

    def test_1(self):
        print(1)

    @unittest.skip('理由是不想執行')  # 無條件跳過用例
    def test_2(self):
        print(2)

    @unittest.skipIf(1 < 2, '符合跳過條件')  # 有條件跳過用例(條件判斷為True就會跳過用例)
    def test_3(self):
        print(3)

    @unittest.skipUnless(1 > 2, '不符合條件')   # 有條件跳過用例(條件判斷為False就會跳過用例)
    def test_4(self):
        print(4)

    @unittest.expectedFailure  # 如果用例failed的話，也不會計入FAILURES中
    def test_5(self):
        print(5)
        self.assertEqual(1, 2, msg='test')


if __name__ == '__main__':
    unittest.main()
