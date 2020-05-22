# 教學網址：http://www.python3.vip/tut/auto/selenium/skills_2/
from selenium import webdriver
import time

driver = webdriver.Chrome(r'd:\Programming\WorkPlace\PythonWork(py37)\Testing\Selenium\chromedriver\chromedriver.exe')
driver.implicitly_wait(5)

driver.get('http://cdn1.python3.vip/files/selenium/test4.html')

# ####################################### alert ###############################################
# 點選alert對象
driver.find_element_by_id('b1').click()

time.sleep(1)

# 打印alert文本
print(driver.switch_to.alert.text)

# 自動幫我們點擊確認紐
driver.switch_to.alert.accept()


# ####################################### confirm(有取消鍵的alert) ###############################################
driver.find_element_by_id('b2').click()

# 打印alert文本
print(driver.switch_to.alert.text)
time.sleep(1)
# 點擊確認紐
driver.switch_to.alert.accept()

driver.find_element_by_id('b2').click()
time.sleep(1)
# 點選取消鈕
driver.switch_to.alert.dismiss()

# ####################################### prompt(有取消鍵和輸入框的alert) ###############################################
driver.find_element_by_id('b3').click()

# 獲取alert對象，這樣之後比較方便
alert = driver.switch_to.alert
# 打印alert文本
print(alert.text)

time.sleep(1)
# 輸入信息
alert.send_keys('123')
time.sleep(1)
# 點擊確認紐
alert.accept()


driver.find_element_by_id('b3').click()
time.sleep(1)
# 點選取消鈕
alert.dismiss()
