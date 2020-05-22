# 教學網址：http://www.python3.vip/tut/auto/selenium/skills_1/
from selenium import webdriver


wd = webdriver.Chrome(r'd:\Programming\WorkPlace\PythonWork(py37)\Testing\Selenium\chromedriver\chromedriver.exe')
wd.implicitly_wait(10)

wd.get('http://cdn1.python3.vip/files/selenium/test2.html')

# 目的：讓所有欄位都只剩下小雷老師
# ####################################### radio ###############################################
# 獲取當前選中欄位
element = wd.find_element_by_css_selector('#s_radio input[checked=checked]')
print('當前是: ' + element.get_attribute('value'))

# 點選 小雷老師
wd.find_element_by_css_selector('#s_radio input[value="小雷老师"]').click()


# ####################################### checkbox ###############################################
# 先把所有已經選中的再點選一次。
elements = wd.find_elements_by_css_selector('#s_checkbox input[checked=checked]')
for e in elements:
    e.click()

# 點選 小雷老師
wd.find_element_by_css_selector('#s_checkbox input[value="小雷老师"]').click()


# ####################################### select單選 ###############################################
"""
select_by_value： 根據選項的value屬性值選擇元素。
select_by_index： 根據選項的次序（從0開始）選擇元素。
select_by_visible_text： 根據選項的可見文本，選擇元素。
deselect_by_value： 根據選項的value屬性值，去除選中元素。
deselect_by_index： 根據選項的次序，去除選中元素。
deselect_by_visible_text： 根據選項的可見文本，去除選中元素。
deselect_all： 去除所有選中元素。
"""
# selenium給我們提供的，方便我們操作
from selenium.webdriver.support.ui import Select

# 創建select對象
# 參數為select的WebElement對象
select = Select(wd.find_element_by_id("ss_single"))

# 通過select對象選擇小雷老師
select.select_by_visible_text("小雷老师")


# ####################################### select多選 ###############################################
from selenium.webdriver.support.ui import Select

# 創建select對象
# 參數為select的WebElement對象
select = Select(wd.find_element_by_id("ss_multi"))

# 去除所有選中元素
select.deselect_all()

# 選擇小雷老师 和 小凯老师
select.select_by_visible_text("小雷老师")
select.select_by_visible_text("小凯老师")
