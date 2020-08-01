// XMLHttpRequest現在已經很少使用了

// 導入xmlhttprequest
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
// 創造一個「XMLHttpRequest」物件，並指派給request變數
var request = new XMLHttpRequest();

// 使用open()函式連接，必要的參數包含「請求方法(‘GET’)」及「API端點的URL」
// 預設使用了 非同步 (async) 的方式接收回應
request.open('GET', 'http://192.168.60.8/r8a-endpoint/value/collection/i/test-station-state-mmcobs');

// 使用非同步，需監聽 load 事件，讓回應完成時能執行相對應的函式 — 回調函式 (callback)
request.onload = function(){
    // 獲取響應頭的Content-Type，以決定如何處理回應
    var content_type = request.getResponseHeader('Content-Type');

    // 使用簡易的正規表達式，判斷媒體類型
    if (content_type.match(/^application\/json/)) {
        jsonHandler(JSON.parse(request.responseText));
    } else if (type.match(/^application\/xml/)) {
        console.log(request.responseXML);
    } else {
        console.log(request.responseText);
    }
};


// send 方法中的參數，是請求訊息的 酬載 (payload) 內容，由於此次使用的是 GET 方法，不得送酬載，因此設為空值
request.send();



// 簡易處理 JSON 回應
function jsonHandler(response) {
    console.log(response);
}



