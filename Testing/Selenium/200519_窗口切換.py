# 教學網址：http://www.python3.vip/tut/auto/selenium/frame/
from selenium import webdriver


wd = webdriver.Chrome(r'd:\Programming\WorkPlace\PythonWork(py37)\Testing\Selenium\chromedriver\chromedriver.exe')
wd.implicitly_wait(10)

wd.get('http://cdn1.python3.vip/files/selenium/sample3.html')
# 先保存著主窗口的handle，方便之後切回來
mainWindow = wd.current_window_handle

# 點擊開啟新窗口連結
link = wd.find_element_by_tag_name("a")
link.click()

# 但這時我們還是只會在原本的那個網頁窗口，
# 如果我們要切換窗口就要透過： wd.switch_to.window(handle)，
# 但因為我們無法獲取特定的handle，只能得到當前瀏覽器裡面所有的窗口handles(WebDriver.window_handles)。
# 所以要透過循環來切換到我們所要切換的窗口。
for handle in wd.window_handles:
    # 切換窗口
    wd.switch_to.window(handle)
    # 透過該窗口的title來判定是不是我們要的
    if 'Bing' in wd.title:
        # 如果是的話，那麼我們只要跳出循環即可，因為這時候WebDriver對象對應的就是我們要的窗口。
        break

# ################################## 在Bing窗口 ###########################################
# wd.title為當前窗口的標記欄(google分頁上顯示的那個標題)
print(wd.title)
wd.find_element_by_id('sb_form_q').send_keys('Jamie\n')
# ################################## 在Bing窗口 ###########################################

# 切回主窗口
wd.switch_to.window(mainWindow)

print(wd.title)
