/*
- 運行前須先把<框架(Django Rest Framework)\200725_權限設計>運行起來
- 練習async/await在非同步請求中的應用
    - async的本質是promise的語法糖，只要function標記為async，就表示裡頭可以撰寫await的同步語法
    - await它會確保一個promise物件都解決(resolve)或出錯(reject)後才會進行下一步
*/

// 導入axios
let axios = require('axios');

async function run(){
    /*
    Description:
        - 主運行函數
        - 採用async函數，可以在底下使用await關鍵字來等待非同步請求的回應
    */
    const credential = await login_and_get_credential('jackooo@kimo.com', 'jack000');
    console.log(credential);
    const user_data = await get_all_specify_user(credential, [1, 2, 4]);
    // console.dir(<要顯示的東西>, {'depth': null}); 可以讓顯示不受深度限制
    console.dir(user_data, {'depth': null});
}

function login_and_get_credential(email, password){
    /*
    Description:
        登入並返回憑證
    Parameter:
        email: 帳號
        password: 密碼
    Return:
        String: 憑證
    */
    let config = {
        headers: { 'Content-Type': 'application/json'},
        timeout: 3000,  // 超時控制(毫秒)
        responseType: 'json',  // 伺服器回應的數據類型
        responseEncoding: 'utf8',  // 伺服器回應的編碼模式
    };
    url = 'http://127.0.0.1:8000/login/';
    data = { 'email': email, 'password': password };

    return axios.post(url, data, config)
    .then((res) => {
        // axios回傳的內容為一個對象(res)，對象包含: data / status / statusText / headers / config 等屬性
        return res.data.token;
    })
    .catch((error) => {
        console.error(error.response.status, error.response.data);
    });
};

function get_all_specify_user(credential, ids){
    /*
    Description:
        - 返回所有指定id的用戶資料
        - 使用axios.all可以同時併發多個請求，並使用axios.spread接收，接收值的順序為發出請求的順序
    Parameter:
        credential: 憑證
        ids: 要回返的所有用戶的id
    Return:
        [Object, Object, ...]: 所有用戶資料
    */
    // 參數...res類似於Python的*args
    return axios.all(ids.map(x => get_specify_user(credential, x)))
    .then(axios.spread((...res) => {
        return res;
    }))
    .catch((err) => { console.error(err) })
}

function get_specify_user(credential, id){
    /*
    Description:
        - 返回指定id的用戶資料
    Parameter:
        credential: 憑證
        id: 要回返用戶的id
    Return:
        Object: 用戶資料
    */
    let config = {
        headers: { 'Authorization': 'JWT '+credential},
    };
    url = 'http://127.0.0.1:8000/api/v1/users/' + id + '/'

    return axios.get(url, config)
    .then((res) => {
        return res.data
    })
    .catch((error) => {
        console.error(error.response.status, error.response.data);
        return error.response.data
    })
};


run();
