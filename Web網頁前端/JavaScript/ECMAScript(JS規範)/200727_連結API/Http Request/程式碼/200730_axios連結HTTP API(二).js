// 練習CRUD，搭配 框架(Django Rest Framework)\200725_權限設計

let axios = require('axios');

function login_and_get_credential(email, password){
    let config = {
        url: 'http://127.0.0.1:8000/login/',
        method: 'post',
        headers: { 'Content-Type': 'application/json'},
        data: { 'email': email, 'password': password },
        timeout: 3000,  // 超時控制(毫秒)
        responseType: 'json',  // 伺服器回應的數據類型
        responseEncoding: 'utf8',  // 伺服器回應的編碼模式
    };

    axios(config)
    .then((res) => {
        // axios回傳的內容為一個對象(res)，對象包含: data / status / statusText / headers / config 等屬性
        console.log(res.data);
        return res.data.token;
    })
    .then((credential) => {
        get_users(credential);
        return credential
    })
    .then((credential) => {
        create_user(credential);
    })
    .catch((error) => {
        console.error(error);
    })
};

function get_users(credential){
    let config = {
        url: 'http://127.0.0.1:8000/api/v1/users/',
        method: 'get',
        headers: { 'Authorization': 'JWT '+credential},
    };

    axios(config)
    .then((res) => {
        // console.dir(res.data, {'depth': null}); 可以讓顯示不受深度限制
        console.dir(res.data, {'depth': null});
    })
    .catch((error) => {
        console.error(error);
    })
};

function create_user(credential){
    let config = {
        url: 'http://127.0.0.1:8000/api/v1/users/',
        method: 'post',
        headers: { 'Authorization': 'JWT '+credential},
        data: { 'email': 'test2ooo@kimo.com', 'password': 'test2000', 'username': 'test2' }
    };

    axios(config)
    .then((res) => {
        console.dir(res.data, {'depth': null});
    })
    .catch((error) => {
        console.error(error.response);
    })
};

function run(){
    login_and_get_credential('jackooo@kimo.com', 'jack000');
};

run();