import jwt
encoded_jwt = jwt.encode({'username': '运维咖啡吧', 'site': 'https://ops-coffee.cn'}, 'secret_key', algorithm='HS256')
print(encoded_jwt)
print(encoded_jwt.decode('utf-8'))
"""
JWT生成的Token是一個用兩個點（.）分割的長字符串
    - 點分割成的三部分分別是Header頭部，Payload負載，Signature簽名：Header.Payload.Signature
    - JWT是不加密的，任何人都可以讀的到其中的信息，其中第一部分Header和第二部分Payload只是對原始輸入的信息轉成了base64編碼，第三部分Signature是用header+payload+secret_key進行加密的結果
"""
import base64
# 因為未加密，所以可以輕易得出原始信息，因此，不適合存放機密性資料
print(base64.b64decode('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'))

# token解碼
# 服務端在有秘鑰的情況下可以直接對JWT生成的Token進行解密，解密成功說明Token正確，且數據沒有被篡改
# secret_key應該設於setting中
print(jwt.decode(encoded_jwt, 'secret_key', algorithms=['HS256']))
