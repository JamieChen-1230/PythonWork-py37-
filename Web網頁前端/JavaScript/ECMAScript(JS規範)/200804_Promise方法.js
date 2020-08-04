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
}

/*
Promise.all:
    - 透過陣列的形式傳入多個 promise 函式
        - 全都Fulfilled: 在全部執行完成後回傳陣列結果，陣列的結果順序與一開始傳入的一致
        - 只要有一個Rejected: 執行onRejected或是.catch
    - 適合用在多支 API 要一起執行，並確保全部完成後才進行其他工作時
*/
//Promise.all([promise(1, 3000), promise(2), promise(3)])
//.then(onFulfilled, onRejected)
//.catch((error) => {
//    console.log(error);
//});


/*
Promise.race:
    - 透過陣列的形式傳入多個promise函式，在全部執行完成後，回傳第一個運行完成的結果
    - 用在站點不穩定，同時發送多支同行為 API 確保可行性使用，但實作中使用率並不高
*/
//Promise.race([promise(0), promise(2), promise(3, 3000)])
//.then(onFulfilled, onRejected)
//.catch((error) => {
//    console.log(error);
//});


/*
Promise.resolve:
    - 一定回傳resolve
    - 參數為回傳值
*/
Promise.resolve('result')
.then(onFulfilled, onRejected);
/*
Promise.reject:
    - 一定回傳reject
    - 參數為回傳值
*/
Promise.reject('result')
.then(onFulfilled, onRejected);


function onFulfilled(res){
    console.log('In onFulfilled:', res);
    return res
};

function onRejected(res){
    console.log('In onRejected:', res);
    return res
};




