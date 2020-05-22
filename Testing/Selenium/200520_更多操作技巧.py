# 教學網址：http://www.python3.vip/tut/auto/selenium/skills_2/
from selenium import webdriver

wd = webdriver.Chrome(r'd:\Programming\WorkPlace\PythonWork(py37)\Testing\Selenium\chromedriver\chromedriver.exe')
wd.implicitly_wait(5)

wd.get('https://www.baidu.com/')

# 這個類裡面提供了很多操作技巧
from selenium.webdriver.common.action_chains import ActionChains

ac = ActionChains(wd)

# 鼠標移動到某個元素上
# 參數為WebElement對象
# 最後一定要調用.perform()才會真正執行
ac.move_to_element(wd.find_element_by_css_selector('[name="tj_briicon"]')).perform()