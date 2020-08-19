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
};

run();