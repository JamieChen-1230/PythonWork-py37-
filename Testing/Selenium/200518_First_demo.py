from selenium import webdriver


# 啟動瀏覽器驅動和瀏覽器，返回的是WebDriver對象
# 參數為chrome驅動的路徑
wd = webdriver.Chrome(r'd:\Programming\WorkPlace\PythonWork(py37)\Testing\Selenium\chromedriver\chromedriver.exe')

# 打開網站
wd.get(url='https://www.google.com.tw/')
# 因為有可能會遇到一種情況，就是web server尚未向我們(用戶)的瀏覽器返回頁面時，我們的程序繼續運行下一行代碼，導致找不到要的Element。
# 所以這時可以使用implicitly_wait(5)，他代表的是最多等5秒，每0.5秒會去搜索一次，如果搜索到了就繼續下一行代碼，反之則等待下一個0.5秒搜索。
wd.implicitly_wait(5)
"""1. 現在在Google首頁"""


"""
整體：
wd.implicitly_wait(5)： 隱式等待
wd.get(url='https://www.google.com.tw/')： 打開網站
wd.title： 當前窗口的標記欄(google分頁上顯示的那個標題)
wd.quit()： 關閉瀏覽器驅動和瀏覽器
wd.current_window_handle： 當前窗口的handle
wd.switch_to.window(handle)： 切換窗口
wd.switch_to.frame('frame的id或WebElement對象')： 切換frame
wd.switch_to.default_content()： 切換回到主Html

選擇元素：
find_element找不到對象返回異常；find_elements找不到對象返回[]。

通過class找第一個對象： find_element_by_class_name
通過class找所有對象(返回列表)： find_elements_by_class_name
通過id找第一個對象： find_element_by_id
通過id找所有對象(返回列表)： find_elements_by_id
通過標籤名(EX:div)找對象： find_element(s)_by_tag_name


操作元素：
點擊對象(通常用於button或a對象)： WebElement對象.click()
輸入字符串： WebElement對象.send_keys()
獲取文本內容(介面上看的到的文本)： WebElement對象.text
獲取元素屬性： WebElement對象.get_attribute(EX:'a')
獲取整個元素對應的HTML文本內容： WebElement對象.get_attribute('outerHTML')
獲取此元素内部所有的HTML文本內容： WebElement對象.get_attribute('innerHTML')
獲取輸入框裡面的文字(不能用.text獲取)： WebElement對象.get_attribute('value')
獲取文本內容(介面上看不到的文本)： WebElement對象.get_attribute('textContent'或'innerText')


CSS選擇器：
通過class找對象： find_element(s)_by_css_selector('.class值')  
通過id找對象： find_element(s)_by_css_selector('#id值')  
通過標籤名找對象： find_element(s)_by_css_selector('標籤名')  
通過屬性找對象： find_element(s)_by_css_selector('[屬姓名]')  EX: [href]，也可以指定值[href="http://www.python3.vip/"]
通過屬性與其他方法混用：find_element(s)_by_css_selector('#id值[屬姓名]'或'.class值[屬姓名]'或'標籤名[屬姓名]')
獲取子元素對象： find_element(s)_by_css_selector('元素1 > 元素2')  EX: #content > span  代表id=content的標籤中標籤名為span的子元素
獲取後代元素對象： find_element(s)_by_css_selector('元素1 元素2')  EX: #content span  代表id=content的標籤中標籤名為span的後代元素
多個查詢加,號(代表或)：find_element(s)_by_css_selector('#aa , div') 
選擇第幾個子元素： find_element(s)_by_css_selector(':nth-child(數字)')  EX: div:nth-child(2)  代表標簽名為div且剛好是在父元素中的第二子元素的標籤
選擇倒數第幾個子元素： find_element(s)_by_css_selector(':nth-last-child(數字)')  
選擇第幾個div子元素： find_element(s)_by_css_selector('div:nth-of-type(數字)')  EX:div:nth-of-type(2)  代表找出子元素中第二個標籤名為div的標籤
選擇倒數第幾個div子元素： find_element(s)_by_css_selector('div:nth-last-of-type(數字)')
選擇第奇數個子元素： find_element(s)_by_css_selector(':nth-child(odd)')
選擇第偶數個子元素： find_element(s)_by_css_selector(':nth-child(even)')
兄弟節點： find_element(s)_by_css_selector('元素1~元素2')  EX:  h3~span  代表找出兄弟節點中有h3的span標籤
相鄰節點： find_element(s)_by_css_selector('元素1+元素2')  EX:  h3+span  代表找出相鄰節點中有h3的span標籤


※ 在瀏覽器中也能透過CSS選擇器來進行查找(非常方便)：
    先按F12  ->  在上面一排選Elements  ->  按 ctrl+f  ->  輸入查詢條件
"""
# 返回WebElement對象。
ele_search = wd.find_element_by_class_name('gLFyf')
# print(ele_search)
# 在輸入框裡輸入"白月黑羽"，並加上Enter鍵(\n)
ele_search.send_keys('白月黑羽\n')


"""2. 現在在Google搜索「白月黑羽」的頁面"""
div = wd.find_element_by_class_name('r')

div.find_element_by_tag_name('a').click()
"""3. 現在在「白月黑羽」首面"""

t = wd.find_element_by_css_selector('.nav-item')

print(t)
# 關閉瀏覽器驅動和瀏覽器
# wd.quit()