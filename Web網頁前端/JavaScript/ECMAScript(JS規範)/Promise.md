# 約定(Promise)

[![hackmd-github-sync-badge](https://hackmd.io/1UXaG3sMSd-39oYkq163wA/badge)](https://hackmd.io/1UXaG3sMSd-39oYkq163wA)


## Promise簡介
### 功能：
- 主要是用來簡化非同步事件之間的嵌套(避免回調地獄)

### 建構Promise物件：
- Promise建構式建立同時，必須傳入一個函式作為參數，此函式被稱為執行器函式(executor function)
- 執行器函式在被建構的當下就會立即被觸發執行
- 執行器函式的參數包含resolve和reject兩個函式
    - resolve(必選)代表的是成功的完成此約定(Promise事件)
    - reject(可選)代表的是此約定中發生錯誤
- resolve和reject僅能運行其中一個，且只能運行一次，回傳後代表此約定(Promise事件)結束
    - resolve函式被運行(呼叫)，代表此Promise事件結束，並進入「已實現」狀態(resolved)
    - reject函式被運行(呼叫)，代表此Promise事件結束，並進入「被拒絕」狀態(rejected)

### 三種返回狀態：
- pending： 事件還在運行中，尚未取得結果
- resolved、fulfilled： 事件已經執行完畢且成功操作，並回傳resolve函式的結果
- rejected： 事件已經執行完畢但操作失敗，並回傳reject函式的結果

### .then方法
- 是一個Promise物件的內建方法
- .then會在上一層的Promise事件結束後被呼叫
- .then可帶入兩個回調函式(函式名可自取)，兩者分別又可以帶入各自的參數
    - onFulfilled(必選)： 在成功(Fulfilled)時執行的函式，此函式帶入的參數為 Promise 函式中 resolve 所帶入的值
    - onRejected(可選)： 在失敗(Rejected)時執行的函式，此函式帶入的參數為 Promise 函式中 reject 所帶入的值
- 結束此次Promise事件：
    - 回傳(return)一個值，代表此Promise事件結束，並進入「已實現」狀態(resolved)
    - 拋出(throw)一個例外，代表此Promise事件結束，並進入「被拒絕」狀態(rejected)

### .catch方法
- 是一個Promise物件的內建方法
- 參數為一個回調函式
- 當前面的.then有寫onRejected函式時，發生rejected會先進到.then，而不是.catch
- 當前面的.then都沒有寫onRejected函式時，發生rejected則會跳到.catch，此回調函式帶入的參數值同樣為 Promise 函式中rejected狀態所返回的值


### .finally方法
- 是一個Promise物件的內建方法
- 回調函式不帶參數
- 通常用來關閉連線(EX:資料庫)等操作

### 流程圖
![](https://i.imgur.com/PP64SI7.png)



&emsp;
## 使用範例
### 定義回調函數(onFulfilled, onRejected)
- 也可以直接寫在裡面，但為了好閱讀，所以提出來
```javascript=
function onFulfilled(res){
    console.log("(Fulfilled)第一層.then:", res);
    return res
};

function onRejected(res){
    console.log("(Rejected)第一層.then:", res);
    throw res;
};
```

### 主要流程：
```javascript=
// resolve,reject 參數名可自定義，但為了好區分通常不會亂取
let p = new Promise(function(resolve, reject){
    const judge = Math.random() > 0.5 ? true : false;

    if(judge){
        // 正確完成的回傳方法
        resolve('Promise成功');
    } else {
        // 失敗的回傳方法
	    reject('Promise失敗');
    };
})
/*
.then：
    - .then會在上一層的Promise事件結束後被呼叫
    - .then可帶入兩個回調函式(函式名可自取)，兩者分別又可以帶入各自的參數
        - onFulfilled(必選)： 在成功(Fulfilled)時執行的函式，此函式帶入的參數為 Promise 函式中 resolve 所帶入的值
        - onRejected(可選)： 在失敗(Rejected)時執行的函式，此函式帶入的參數為 Promise 函式中 reject 所帶入的值
    - 結束此次Promise事件：
        - 回傳(return)一個值，代表此Promise事件結束，並進入「已實現」狀態(resolved)
        - 拋出(throw)一個例外，代表此Promise事件結束，並進入「被拒絕」狀態(rejected)
*/
.then(onFulfilled, onRejected)
/*
可以一直.then下去，
    - 當上層進入resolved時，也就是使用了return，表示上層Promise事件結束，且會進入到下層Promise事件，並被onFulfilled函式接收到
        - return的回傳值會變成下層onFulfilled函式的參數值
    - 當上層進入rejected時，也就是使用了throw，表示上層Promise事件結束，且會進入到下層Promise事件，並被onRejected函式接收到
        - throw的錯誤值會變成下層onRejected函式的參數值
*/
.then(function(res){
    // 只有onFulfilled函式，所以當上層Rejected時，會被後面.then中的onRejected函式接收到或是直接進入到.catch
    console.log("(Fulfilled)第二層.then:", res);
    return res;
})
.then((res) => {
    console.log("(Fulfilled)第三層.then:", res);
    return res;
}, (error) => {
    console.log("(Rejected)第三層.then:", error);
    throw error;
})
/*
.catch：
    - 參數為一個回調函式，
    - 當前面的.then有寫onRejected函式時，發生rejected會先進到.then，而不是.catch
    - 當前面的.then都沒有寫onRejected函式時，發生rejected則會跳到.catch，此回調函式帶入的參數值同樣為 Promise 函式中rejected狀態所返回的值
*/
.catch(function(error){
   console.log(".catch:", error);
})
/*
.finally中的回調函式不帶參數
    - 通常用來關閉讀取等操作
*/
.finally(function(){
    console.log("finally");
});
```


&emsp;
## 其他Promise方法
### Promise.all:
- 透過陣列的形式傳入多個 promise 函式
    - 全都Fulfilled才會在全部執行完成後回傳陣列結果，陣列的結果順序與一開始傳入的一致
    - 只要有一個Rejected就會執行onRejected或是.catch
- 適合用在多支 API 要一起執行，並確保全部完成後才進行其他工作時
- 範例：
```javascript=
function promise(num, time = 500) {
    let p = new Promise((resolve, reject) => {
        // setTimeout()的作用是在延遲了某段時間(單位為毫秒)之後，才去執行「一次」指定的程式碼
        setTimeout(() => {
          if(num >= 1){
            resolve(`${num}, 成功`)
          }else{
            reject('失敗');
          };
        }, time);
    });
  return p;
};

Promise.all([promise(1, 3000), promise(2), promise(3)])
.then(onFulfilled, onRejected)
.catch((error) => {
   console.log(error);
});
```

### Promise.race:
- 透過陣列的形式傳入多個promise函式，在全部執行完成後，回傳第一個運行完成的結果
- 用在站點不穩定，同時發送多支同行為 API 確保可行性使用，但實作中使用率並不高
- 範例：
```javascript=
function promise(num, time = 500) {
    let p = new Promise((resolve, reject) => {
        // setTimeout()的作用是在延遲了某段時間(單位為毫秒)之後，才去執行「一次」指定的程式碼
        setTimeout(() => {
          if(num >= 1){
            resolve(`${num}, 成功`)
          }else{
            reject('失敗');
          };
        }, time);
    });
  return p;
};

Promise.race([promise(0), promise(2), promise(3, 3000)])
.then(onFulfilled, onRejected)
.catch((error) => {
   console.log(error);
});
```

### Promise.resolve:
- 一定回傳resolve
- 參數為回傳值
- 範例：
```javascript=
function onFulfilled(res){
    console.log('In onFulfilled:', res);
    return res
};

function onRejected(res){
    console.log('In onRejected:', res);
    return res
};

Promise.resolve('result')
.then(onFulfilled, onRejected);
```
    
### Promise.reject:
- 一定回傳reject
- 參數為回傳值
```javascript=
function onFulfilled(res){
    console.log('In onFulfilled:', res);
    return res
};

function onRejected(res){
    console.log('In onRejected:', res);
    return res
};

Promise.reject('result')
.then(onFulfilled, onRejected);
```


&emsp;
## Promise搭配Async/Await

### 簡介：
- Async
    - 用來裝飾函數，使它變成一個異步函數
    - async函數返回的是一個Promise對象，因此也可以使用.then方法
        - 如果async函式回傳了一個值，Promise的狀態將為一個帶有該回傳值的resolved
        - 如果async函式拋出例外或某個值，Promise的狀態將為一個帶有被拋出值的rejected
- Await
    - 只能用於異步函數中
    - 使用await會暫停此async函數的執行，並且等待傳遞至表達式的Promise的解析，解析完之後會回傳解析值，並繼續此async函數的執行
    - 使用await時，最好用try...catch包起來，因為有可能會是rejected

### 範例：
```javascript
function promise(num, timeout=500) {
    let p = new Promise((resolve, reject) => {
        // setTimeout()的作用是在延遲了某段時間(單位為毫秒)之後，才去執行「一次」指定的程式碼
        setTimeout(() => {
            resolve(`${num}成功`)
        }, timeout);
    });
  return p;
};

async function run(){
    try {
        const result_with_no_await = Promise.all([promise(1, 3000), promise(2), promise(3)])
        .then(([res1, res2, res3]) => {
            return [res1, res2, res3];
        });
        // 因為沒有使用await關鍵字去等待，result_with_no_await的結果還沒出來，所以會返回 Promise { <pending> }
        console.log(result_with_no_await);

        const result_with_await = await Promise.all([promise(1, 3000), promise(2), promise(3)])
        .then(([res1, res2, res3]) => {
            return [res1, res2, res3];
        });
        // 因為有使用await關鍵字，所以程序會等result_with_await回傳後再繼續進行，有接收到值[ '1成功', '2成功', '3成功' ]
        console.log(result_with_await);
    } catch (error) {
        console.log(error);
    }
};

run();
```













###### tags: `JavaScript`