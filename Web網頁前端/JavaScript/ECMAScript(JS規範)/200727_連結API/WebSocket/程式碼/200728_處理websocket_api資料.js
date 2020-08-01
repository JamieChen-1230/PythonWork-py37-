var url = 'ws://192.168.60.8/r8a-websocket/value/subscribe';
var WebSocket = require('ws');
var socket = new WebSocket(url);
var msg = {
      // 不知
      "from": 0,
      // 中心
      "collections": [
        {
          "collection_ident": "servers-mmcobs"
        },
        // {
        //   "collection_ident": "test-station-state-mmcobs"
        // }
      ],
    }
var jsonMsg = JSON.stringify(msg);

socket.onopen = function(e) {
  console.log('與服務端連結成功');
  socket.send(jsonMsg);
};

socket.onmessage = function(event) {
  console.log('服務端有一條訊息返回');
  filterData(event.data);
};

socket.onclose = function(event) {
  if (event.wasClean) {
    console.log(`[關閉連線] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
  } else {
    console.log('[關閉連線] Connection died');
  }
};

socket.onerror = function(error) {
  console.log(`[錯誤] ${error.message}`);
};

function filterData(json_data){
  let data = JSON.parse(json_data);  // 將 JSON 字串解析成 JavaScript 物件
  // console.log(data['result_code']);
  // console.log(data['collection_values'])
  let complex_idents = []
  for(let id in data['collection_values']['complex_values']){
    dicData = data['collection_values']['complex_values'][id]
    console.log(id);
    for(let key in dicData){
      console.log(key, dicData[key]);
      if(key=='complex_ident'){
        complex_idents.push(dicData[key]);
      }
    }
  }
  console.log(complex_idents);
  
};