// axios是現代較為推薦的資源請求方式

// 導入axios
// import axios // 報錯，LTS版目前還未支持import語法
let axios = require('axios');

// // 基本用法
// var url = 'http://192.168.60.8/r8a-endpoint/value/collection/i/test-station-state-mmcobs';
// // 使用axios發送get請求
// axios.get(url)
// // axios回傳的內容為一個對象，對象包含: data / status / statusText / headers / config 等屬性
// .then((res) => { 
//     // console.table(res.data);
//     console.log(res.data); 
// })
// .catch((error) => {
//         console.error(error);
// })
// .finally(() => {
//         console.log('不論失敗成功與否皆會執行');
// });


// 使用config用法
const config = {
    url: '/r8a-endpoint/value/collection/3/test-station-state-mmcobs',  // 只有url為必填
    method: 'get', // 大小寫皆可
    headers: { 'Content-Type': 'application/json' },

    // 添加在 url 前面，除非 url 為絕對路徑
    baseURL: 'http://192.168.60.8',

    // 主要傳送的資料 (用於 PUT、POST、PATCH )
    // 在沒有 transformRequest 情況下資料型別有限制 (下有補充)
    // data: { name: 'test', title: 777 },

    // 此為GET請求參數
    // params: { ID: 123 },

    // 序列化參數
    // paramsSerializer: function(params) {
    //     return Qs.stringify(params, {arrayFormat: 'brackets'})
    // },

    maxContentLength: 200000000000, // 限制傳送大小
        
    // 請求時間超過5000毫秒(5秒)，請求會被中止
    timeout: 5000,

    // 選項: 'arraybuffer', 'document', 'json', 'text', 'stream'
    // 瀏覽器才有 'blob' ， 預設為 'json'
    responseType: 'json', // 伺服器回應的數據類型

    // 伺服器回應的編碼模式 預設 'utf8'
    responseEncoding: 'utf8',

    // 在上傳、下載途中可執行的事情 (progressBar、Loading)
    onUploadProgress(progressEvt) { /* 原生 ProgressEvent */  },
    onDownloadProgress(progressEvt) { /* 原生 ProgressEvent */ },

    // 允許自定義處理請求，可讓測試更容易 (有看沒懂..)
    // return promise 並提供有效的回應 (valid response)
    // adapter (config) { /* 下方章節 補充詳細用法 */ },
};

axios(config)
// axios回傳的內容為一個對象，對象包含: data / status / statusText / headers / config 等屬性
.then((res) => { 
    // console.table(res.data);
    console.dir(res.data, {'depth': null});
    // console.log(res.data.complex_values);
    // for(let i in res.data.complex_values){
    //     console.log(res.data.complex_values[i].tracked_values);
    // } 

})
.catch((error) => {
        console.error(error);
})
.finally(() => {
        console.log('不論失敗成功與否皆會執行');
});
