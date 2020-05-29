import unittest
from selenium import webdriver
import time


# 測試用例類(必須繼承Unuttest TestCase類)
class MyTestCase(unittest.TestCase):

    def test_a(self):
        self.driver = webdriver.Chrome(r'd:\Programming\WorkPlace\PythonWork(py37)\Testing\Selenium\chromedriver\chromedriver.exe')
        self.driver.get(url='https://www.google.com.tw/')
        self.driver.find_element_by_class_name('gLFyf').send_keys('虛竹\n')
        time.sleep(2)
        self.driver.quit()

    def test_b(self):
        self.driver = webdriver.Chrome(r'd:\Programming\WorkPlace\PythonWork(py37)\Testing\Selenium\chromedriver\chromedriver.exe')
        self.driver.get(url='https://www.google.com.tw/')
        self.driver.find_element_by_class_name('gLFyf').send_keys('巴哈\n')
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
