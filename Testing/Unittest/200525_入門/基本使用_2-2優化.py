import unittest
from selenium import webdriver
import time
import ddt


# 測試用例類(必須繼承Unuttest TestCase類)
@ddt.ddt  # 要在用例中使用ddt，需要先在測試類上導入ddt(@ddt.ddt)
class MyTestCase(unittest.TestCase):
    # 啟動Chrome驅動和瀏覽器並跳轉到google首頁
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(r'd:\Programming\WorkPlace\PythonWork(py37)\Testing\Selenium\chromedriver\chromedriver.exe')
        self.driver.get(url='https://www.google.com.tw/')

    # 關閉驅動
    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()

    # # 測試用例中最好只放真正執行的操作(這樣代碼簡潔又易維護)
    @ddt.data('虛竹', 'msi', 'python')  # 循環傳入參數，這邊執行了3次test_a，參數則依序使用@ddt.data中的數據
    def test_a(self, txt):
        self.driver.find_element_by_class_name('gLFyf').send_keys(txt)

    @ddt.data(('msi', 'python'), ('java', 'python'))
    @ddt.unpack  # 如果要傳的參數不只一個，那就需要使用到@ddt.unpack
    def test_b(self, txt1, txt2):
        txt = txt1 + txt2
        self.driver.find_element_by_class_name('gLFyf').send_keys(txt)


if __name__ == '__main__':
    unittest.main()
