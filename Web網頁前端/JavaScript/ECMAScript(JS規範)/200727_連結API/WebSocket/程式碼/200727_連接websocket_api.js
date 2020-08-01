var url = 'ws://192.168.60.8/r8a-websocket/value/subscribe';
var WebSocket = require('ws');
var socket = new WebSocket(url);
var data = {
      // 不知
      "from": 0,
      // 中心
      "collections": [
        {
          "collection_ident": "servers-mmcobs"
        },
        // {
        //   "collection_ident": "test-data-receive-mmcobs"
        // },
        // {
        //   "collection_ident": "test-product-build-mmcobs"
        // },
        // {
        //   "collection_ident": "test-station-state-mmcobs"
        // }
      ],
      // 不知
      // "tracked_raws": [
      //   {
      //     "tracked_value_access_ident": "xmlDaKYMg03dqr58TyqpUgIAAAA",
      //     "fix_span_seconds": 86400,
      //     "subscriber_ref": {"frontend_data": 2}
      //   },
      //   {
      //     "tracked_value_access_ident": "xmlDaKYMg03dqr58TyqpUgQAAAA",
      //     "fix_span_seconds": 86400
      //   }
      // ]
    }
var jsonData = JSON.stringify(data);

socket.onopen = function(e) {
  console.log('open connection');
  socket.send(jsonData);
};

socket.onmessage = function(event) {
  console.log(event.data)
};

socket.onclose = function(event) {
  if (event.wasClean) {
    console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
  } else {
    console.log('[close] Connection died');
  }
};

socket.onerror = function(error) {
  console.log(`[error] ${error.message}`);
};