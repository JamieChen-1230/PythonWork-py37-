/*
約定(Promise)：
    - 功能：
        - 主要是用來簡化非同步事件的嵌套
    - 建構Promise物件：
        - Promise建構式建立同時，必須傳入一個函式作為參數，此函式被稱為執行器函式(executor function)
        - 執行器函式在被建構的當下就會立即被觸發執行
        - 執行器函式的參數包含resolve和reject兩個函式
            - resolve(必選)代表的是成功的完成此約定(Promise事件)
            - reject(可選)代表的是此約定中發生錯誤
        - resolve和reject僅能運行其中一個，且只能運行一次，回傳後代表此約定(Promise事件)結束
            - resolve函式被運行(呼叫)，代表此Promise事件結束，並進入「已實現」狀態(resolved)
            - reject函式被運行(呼叫)，代表此Promise事件結束，並進入「被拒絕」狀態(rejected)
    - 三種狀態：
        - pending： 事件還在運行中，尚未取得結果
        - resolved、fulfilled： 事件已經執行完畢且成功操作，並回傳resolve函式的結果
        - rejected： 事件已經執行完畢但操作失敗，並回傳reject函式的結果
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
.then：
    - 是一個Promise物件的內建方法
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



function onFulfilled(res){
    console.log("(Fulfilled)第一層.then:", res);
    return res
};

function onRejected(res){
    console.log("(Rejected)第一層.then:", res);
    throw res;
};


