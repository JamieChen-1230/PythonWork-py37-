# 教學網址：http://www.python3.vip/tut/auto/selenium/frame/
from selenium import webdriver


# 啟動瀏覽器驅動和瀏覽器，返回的是WebDriver對象
# 參數為chrome驅動的路徑
wd = webdriver.Chrome(r'd:\Programming\WorkPlace\PythonWork(py37)\Testing\Selenium\chromedriver\chromedriver.exe')

wd.get('http://cdn1.python3.vip/files/selenium/sample2.html')


# 因為在html語法中，frame元素或者iframe元素的內部會包含一個被嵌入的另一份html文檔。
# 而我們在查找元素時只會找到最外層的HTML文檔，因此要找到frame的元素的話，必須先切換至frame裡的html文檔。
# 切換至frame裡的html文檔： wd.switch_to.frame('frame的id或WebElement對象')
# wd.switch_to.frame('frame1')  # 用id
wd.switch_to.frame(wd.find_element_by_css_selector('iframe[src="sample1.html"]'))  # 用WebElement對象

# ############################# iframe中 ##################################
element = wd.find_elements_by_css_selector('.plant')

for e in element:
    print(e.get_attribute('outerHTML'))
# ############################# iframe中 ##################################

# 切換回到主Html
wd.switch_to.default_content()
wd.find_element_by_id('outerbutton').click()

# wd.quit()
