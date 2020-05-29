import unittest
import ddt


# 測試用例類(必須繼承Unuttest TestCase類)
@ddt.ddt  # 要在用例中使用ddt，需要先在測試類上導入ddt(@ddt.ddt)
class MyTestCase(unittest.TestCase):

    # 循環傳入參數，這邊執行了3次test_a，參數則依序使用@ddt.data中的數據
    @ddt.data('虛竹', 'msi', 'python')
    def test_a(self, txt):
        print(txt)


if __name__ == '__main__':
    unittest.main()
