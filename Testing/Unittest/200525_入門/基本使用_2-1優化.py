import unittest
from selenium import webdriver
import time


# 測試用例類(必須繼承Unuttest TestCase類)
class MyTestCase(unittest.TestCase):
    # 啟動Chrome驅動和瀏覽器並跳轉到google首頁
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(r'd:\Programming\WorkPlace\PythonWork(py37)\Testing\Selenium\chromedriver\chromedriver.exe')
        self.driver.get(url='https://www.google.com.tw/')

    # 關閉驅動
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    # 測試用例中最好只放真正執行的操作(這樣代碼簡潔又易維護)
    def test_a(self):
        self.driver.find_element_by_class_name('gLFyf').send_keys('虛竹\n')

    def test_b(self):
        self.driver.find_element_by_class_name('gLFyf').send_keys('巴哈\n')


if __name__ == '__main__':
    unittest.main()
