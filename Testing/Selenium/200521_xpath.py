# 教學網址：http://www.python3.vip/tut/auto/selenium/xpath_1/
from selenium import webdriver


driver = webdriver.Chrome(r'd:\Programming\WorkPlace\PythonWork(py37)\Testing\Selenium\chromedriver\chromedriver.exe')
driver.implicitly_wait(10)

driver.get('http://cdn1.python3.vip/files/selenium/test1.html')
"""
(建議使用它)
XPath (XML Path Language) 是由國際標準化組織(W3C)指定用來在XML 和HTML 文檔中選擇節點的語言。
在自動化中使用 WebbElement對象.find_element(s)_by_xpath() 來調用xpath。
    
HTML文檔的根節點： /
當前對象(EX：.//div  代表當前對象下的所有div元素)： .   
通配符(代表所有對象)(EX： //div/*  代表div之下的所有元素)： *
選擇html中的body中的div元素： /html/body/div
    - 相當於CSS選擇器的 html>body>div
    - 相當於找子元素
找子元素： /div
找後代元素(相對路徑)： //div
屬性查找： [@屬性名="屬性值"]
    - /div[@class="li"]  代表子元素中的div標籤且id="li"
    - /div[@id="1"][@class="li"]  多條件：代表子元素中的div標籤且id="1"且class="li"
    - //*[@name="aa"]  代表所有name="aa"的元素
    - //*[@href]  代表所有有href屬性的元素
    - //p[@class="capital huge-city"]  如果class包含多個值，不能只寫其中一個，一定要寫全部
        - 在這方面CSS選擇器做得比較好，可以透過單個值查詢。
        
屬性值進階查找：
    - //*[contains(@style,'color')]  代表所有style屬性值包含color字符串的元素
    - //a[starts-with(@href, '/all/hot/recent/')]  找到href開頭為/all/hot/recent/的所有a元素
    - //a[re:test(@href, '/all/hot/recent/\d+')]  用正則找到href為/all/hot/recent/\d+的所有a標籤
    - xpath 1中沒有以結尾做查找的方式。
        - CSS選擇器中有： a[href$="123"]

按次序選擇：
    - //p[2]  代表第二個p類型的元素
    - //div/*[last()]  代表所有div下的最後一個元素
    - //div/*[last()-1]  代表所有div下的倒數第二個元素
    
範圍選擇(從1開始)：
    - //div/option[position()<=2]  代表所有div下第1, 2個option元素
    - //*[@class='multi_choice']/*[position()>=last()-2]  代表class屬性為multi_choice的後3個子元素
"""

elements = driver.find_elements_by_xpath("/html/body/div")

for e in elements:
    print(e.get_attribute('outerHTML'))


driver.quit()
