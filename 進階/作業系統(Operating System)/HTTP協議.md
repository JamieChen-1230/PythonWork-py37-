# HTTP協議

## Http(超文本傳輸協定)：
### 概述：
- 是一種用來傳輸超媒體文件(像是HTML文件)的協定，被設計來讓瀏覽器和伺服器進行溝通。
- 內容規範了客戶端請求與伺服器回應的標準，通常使用 TCP 作為資料的傳輸方式。
### 請求方法(8種)：
- GET： 向指定的資源發出「顯示」請求，通常GET方法應該只用在查詢讀取資料
- POST： 向指定資源提交資料，請求伺服器進行處理，而資料放在請求體中
- PUT： 向指定資源位置上傳其最新內容(覆蓋資源)
- PATCH： 用於將局部修改應用到資源(一般常見定義上的修改)
- DELETE： 請求伺服器刪除Request-URI所標識的資源
- 不常用的： 
    - TRACE(用於測試或診斷)
    - HEAD(向伺服器發出指定資源的請求)
    - CONNECT
### HTTP請求：
#### 請求行：
- 組成： 請求方法 URL 協議/版本
- 範例： POST /index.php HTTP/1.1
- 請求方法： GET、POST、HEAD、OPTIONS、PUT、DELETE和TARCE等
- URL： 指定了要訪問的網絡資源，通常只要給出伺服器根目錄的相對目錄即可，因此總是以「/」開頭
- 協議版本： 聲明了通信過程中使用HTTP的版本
#### 請求頭：
- 組成： 域名 冒號(:) 域值
- 範例： accept-encoding: gzip
- 常見的請求頭：
    - Connection：
        - 作用： 表示是否需要持久連接。
        - 域值：
            - Connection: keep-alive：
                當網頁打開完成後，客戶端和伺服器之間用於傳輸HTTP數據的TCP連接不會關閉，
                如果客戶端再次訪問這個伺服器上的網頁，會繼續使用這一條已經建立的連接。
            - Connection: close：
                代表一個Request完成後，客戶端和伺服器之間用於傳輸HTTP數據的TCP連接會關閉，
                當客戶端再次發送Request，需要重新建立TCP連接。
    - Host(發送請求時，此頭域是必須的)：
        - 作用： 用於指定被請求資源的Internet主機和埠號，它通常從請求行的URL中提取出來的。
    - Accept：
        - 作用： 指定瀏覽器可以接受的媒體類型(也可以說是希望伺服器響應的類型)
        - 範例：
            - Accept: text/html
                代表瀏覽器可以接受伺服器回發的類型為text/html，也就是我們常說的html文檔，
                如果伺服器無法返回text/html類型的數據，伺服器應該返回一個406錯誤(non acceptable)。
            - Accept: */*
                代表瀏覽器可以處理所有類型(一般瀏覽器發給伺服器都是發這個)。
    - Accept-Encoding：
        - 作用： 瀏覽器聲明自己接收的編碼方法，通常是指壓縮方法(是否支持壓縮，支持什麼壓縮方法)。
        - 範例：
            - Accept-Encoding: gzip, deflate
                伺服器能夠向支持gzip/deflate的瀏覽器返回經gzip或者deflate編碼的HTML頁面，
                通常情形下，壓縮可以減少5到10倍的下載時間，也節省帶寬。
    - Accept-Language：
        - 作用： 瀏覽器聲明自己接收的語言。
        - 範例：
            - Accept-Language: zh-cn
                如果請求消息中沒有設置這個頭域，伺服器假定客戶端對各種語言都可以接受。
    - Accept-Charset：
        - 作用： 瀏覽器申明自己接收的字符集(EX: gb2312，utf-8)。
        - 範例：
            - Accept-Charset: iso-8859-1,gb2312
                如果在請求消息中沒有設置這個域，預設是任何字符集都可以接受。
    - User-Agent：
        - 作用： 告訴伺服器，客戶端使用的作業系統和瀏覽器的名稱和版本
        - 範例：
            - User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36
    - Authorization：
        - 作用： 用於證明客戶端有權查看某個資源。
               當瀏覽器訪問一個頁面時，如果收到伺服器的響應代碼為401(未授權)，
               可以發送一個包含Authorization請求報頭域的請求，要求伺服器對其進行驗證。
    - Cookie：
        - 作用： 將cookie的值發送給HTTP伺服器。
    - Content-Length：
        - 作用： 發送給HTTP伺服器數據的長度，即請求體正文的長度。
    - Referer：
        - 作用： 提供了Request的上下文信息的伺服器。
        - 範例：
            - Referer: http://translate.google.cn/?hl=zh-cn&tab=wT
                告訴伺服器我是從哪個連結過來的，比如從我主頁上連結到一個朋友那裡，
                他的伺服器就能夠從HTTP Referer中統計出每天有多少用戶點擊我主頁上的連結訪問他的網站。
    - Content-Type：
        - 作用： 代表發送端發送的實體數據的數據類型(規定請求體中的數據格式)。
        - 範例：
            - Content-Type: application/x-www-form-urlencoded
#### 請求體：
- 不是必須的，可以為空。
- 請求體中承載多個請求參數的數據。
- 請求體中的參數數據格式，必須根據請求頭中的Content-Type設置。
    - 範例：
        Content-Type: application/x-www-form-urlencoded
        數據格式： name=jamie&age=18&height=179
### HTTP響應：
#### 狀態行：
- 組成： 協議版本 數字形式的狀態碼(Status-Code) 相應的狀態描述
- 範例：  HTTP/1.1 200 OK
#### 響應頭：
- 常見的響應頭：
    - Date：
        - 作用：生成消息的具體時間和日期，即當前的GMT時間。
        - 範例： Date: Sun, 17 Mar 2013 08:12:54 GMT
    - Expires：
        - 作用： 瀏覽器會在指定過期時間內使用本地緩存，指明應該在什麼時候認為文檔已經過期，從而不再緩存它。
        - 範例： Expires: Thu, 19 Nov 1981 08:52:00 GMT　
    - Set-Cookie：
        - 作用： 非常重要的header，用於把cookie發送到客戶端瀏覽器，每一個寫入cookie都會生成一個Set-Cookie。
        - 範例： Set-Cookie: PHPSESSID=c0huq7pdkmm5gg6osoe3mgjmm3; path=/
    - Content-Type：
        - 作用： WEB伺服器告訴瀏覽器自己響應的對象的類型和字符集。
        - 範例：
            - Content-Type: text/html; charset=utf-8
                表示響應體是一個HTML文檔，且編碼為UTF-8。
    - Content-Encoding：
        - 作用： 文檔的編碼(Encode)方法，一般是壓縮方式。
        - 範例： Content-Encoding：gzip
    - Server：
        - 作用： 指明HTTP伺服器的軟體信息。
        - 範例： Apache/2.2.8 (Win32) PHP/5.2.5
#### 響應體：
- 就是伺服器返回的資源的內容。
- 數據格式，必須根據響應頭中的Content-Type。


## 差異比較
### GET和POST比較：
- GET資料傳遞方式是將參數以key/value的方式，透過URL帶至Server端；
  POST資料傳遞方式是將參數放至請求體中，因此不會在URL看到參數，較為隱密
- POST的安全性要比GET的安全性高，因為GET傳遞的參數會在URL上顯示
- GET傳遞的參數會被儲存在瀏覽器的歷史紀錄中；POST則不會
- GET只允許傳輸ASCII的資料；POST則不限
- GET參數長度會受到瀏覽器的限制；POST則不會


### POST和PUT比較：
- 兩者其實都可以用來新增資源，但PUT會比較像是覆蓋或替代資源
- PUT會指定要覆蓋掉哪個資源，POST則不用
- 如果假設資料庫不能有重複資料的話，用POST新增多個可能會報錯，但PUT不會，因為它只是不停的對某個資源進行覆蓋而已


### TCP和UDP比較：
#### TCP(傳輸控制協定)：
- 是一種可靠的網路通訊協定，所以為了保證不發生丟包，會給每個包一個序號，同時序號也保證了傳送到接收端實體的包的按序接收。
    - 一、連線機制(三手交握)：
        - A發起連線請求
        - B返回連線確認
        - A發送連線成功信息
    - 二、內容傳輸：
        - 確認封包機制： 接收端接收到包時要回傳確認信息給發送端
        - 逾時與重送： 若接收端一直無返回確認信息，發送端則會重發一次
    - 三、斷開機制(四次揮手)：
        - A發送斷開請求
        - B返回確認信息
        - 等待B也處理完後，B也發送斷開請求
        - A返回確認信息
#### UDP： 
- 是一種非可靠的網路通訊協定，因為沒有確認機制，所以開銷較低，速度較快，通常用來做一些語音、影像的傳遞。



##### tags `HTTP` `OS`