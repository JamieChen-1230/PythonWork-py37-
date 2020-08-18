# Axios

### 觀看本文前，能先去看另一個筆記(Promise)，會更好了解。
- 傳送門：
[![hackmd-github-sync-badge](https://hackmd.io/1UXaG3sMSd-39oYkq163wA/badge)](https://hackmd.io/1UXaG3sMSd-39oYkq163wA)

&emsp;
## Axios簡介

### 用途：
- Axios是一個基於Promise用於瀏覽器和nodejs的HTTP客戶端，簡單的說，就是可以利用它來發送get、post等HTTP請求

### 特點：
- 基於promise的異步請求庫
- 瀏覽器端和node端皆可以使用
- 支持請求和響應攔截器
- 支持請求取消
- 自動轉換成JSON資料類型
- 支持批量發送多個請求

### 安裝：
```
npm install axios
```

&emsp;
## 使用
### 基礎使用：
- 方式一：
    - 用法：
        - axios.<HTTP方法>()
    - 請求方法別名：
        - axios.get（url [, config]）
        - axios.delete（url [, config]）
        - axios.head（url [, config]）
        - axios.post（url [, data [, config]]）
        - axios.put（url [, data [, config]]）
        - axios.patch（url [, data [, config]]）
    - ※ 當使用別名方法時，不需要在config中指定url，method和data屬性
    - 範例：
    ```javascript
    let axios = require('axios');

    var url = 'https://github.com/JamieChen-1230';
    
    axios.get(url)
    .then((res) => { 
        // resolved時執行
        // axios回傳的內容為一個對象，對象包含: data / status / statusText / headers / config 等屬性
        console.log(res.data); 
    })
    .catch((error) => {
        // rejected時執行
        console.error(error);
    })
    .finally(() => {
        console.log('不論失敗成功與否皆會執行');
    });
    ```
&emsp;
- 方式二(所有資訊都寫在config裡)：
    - 用法：
        - axios.request(config)
    - 範例：
    ```javascript
    let axios = require('axios');

    const config = {
        // 只有url為必填
        url: 'JamieChen-1230',  

        // 大小寫皆可
        method: 'get', 

        // 請求頭設置
        headers: { 'Content-Type': 'application/json' },

        // 添加在url前面，除非url為絕對路徑
        baseURL: 'https://github.com/',
        
        // 請求體 (適用於 PUT、POST、PATCH等)
        // data: { name: 'test', title: 777 },

        // URL參數(適用於GET)
        // params: { ID: 123 },

        // 限制傳送資料大小
        // maxContentLength: 2000, 

        // 請求時間超過5000毫秒(5秒)，請求會被中止
        timeout: 5000,

        // 伺服器回應的數據類型
        // 選項: 'arraybuffer', 'document', 'json', 'text', 'stream'
        // 瀏覽器才有'blob'，預設為'json'
        responseType: 'json', 

        // 伺服器回應的編碼模式 預設'utf8'
        responseEncoding: 'utf8',
    };

    axios.request(config)
    .then((res) => { 
        // resolved時執行
        // axios回傳的內容為一個對象，對象包含: data / status / statusText / headers / config 等屬性
        console.dir(res.data, {'depth': null});
    })
    .catch((error) => {
        // rejected時執行
        console.error(error);
    })
    .finally(() => {
        // 不論失敗成功與否皆會執行
        console.log('不論失敗成功與否皆會執行');
    });
    ```



###### tags: `JavaScript`

&emsp;
### 進階使用：
- 多併發axios請求：
    - 使用axios.all()一次發出多個異步請求
    - 透過axios.spread()有順序的接收回傳值
    - 範例：
    ```javascript
    let axios = require('axios');
    
    function func1(){
      return axios.get('https://github.com/JamieChen-1230');
    }
    function func2(){
      return axios.get('https://github.com/JamieChen-1230');
    }
    
    axios.all([func1(), func2()])
    .then(axios.spread(function(res1, res2){
        // res是依照發出請求的順序對應，而不是請求響應的先後順序
        // res1 => func1(), res2 => func2()
        console.log(res1, res2);
    }));
    ```