/*
Promise：
    - 功能：
        - 主要是用來處理非同步的事件
    - 建構：
        - 建構函式建立同時，必須傳入一個函式作為參數（executor function）
        - 函式的參數包含resolve和reject，這兩個方法分別代表成功與失敗的回傳結果
        - return時，resolve和reject僅能回傳其中之一，且必定只能回傳一次，回傳後代表此 Promise 事件結束
    - 狀態：
        - pending： 事件已經運行中，尚未取得結果
        - resolved： 事件已經執行完畢且成功操作，回傳 resolve 的結果（該承諾已經被實現 fulfilled）
        - rejected： 事件已經執行完畢但操作失敗，回傳 reject 的結果
*/

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
.then可帶入兩個回調函數(函數名可自取)，兩者分別又可以帶入各自的參數
    - onFulfilled： 執行成功的函式，此函數帶入的參數為 Promise 函式中 resolve 所帶入的值
    - onRejected： 執行失敗的函式，此函數帶入的參數為 Promise 函式中 reject 所帶入的值
*/
.then(onFulfilled, onRejected)
/*
- 可以一直.then下去，下層.then的參數值為上層.then的回傳值
- 當只有一個函數時，不管是onFulfilled還是onRejected都會接收到
*/
.then(function(res){
    console.log("第二層.then:", res);
    return res;
})
/*
.catch帶入一個回調函數(函數名可自取)，
    - 當前面的.then有寫onRejected函數時，發生rejected會進到.then，而不是.catch
    - 當前面的.then都沒有寫onRejected函數時，發生rejected會跳到.catch，此函數帶入的參數同樣為 Promise 函式中 reject 所帶入的值
*/
.catch(function(error){
   console.log(".catch:", error);
})
/*
.finally中的回調函數不帶參數
    - 通常用來關閉讀取等
*/
.finally(function(){
    console.log("finally");
});



function onFulfilled(res){
    console.log("第一層.then:", res);
    return res
};

function onRejected(res){
    console.log("第一層.then:", res);
    return res
};


