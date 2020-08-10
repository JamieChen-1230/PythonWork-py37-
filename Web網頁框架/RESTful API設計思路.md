# RESTful API設計思路

## 定義需求：
   - 是否有需要使用權限認證
   - 有哪些資源需定義

## 設定資源來源：
   - 資料庫
      - 設計資料表
   - 上游API
      - 思考要如何取出自己要的部分資料

## 設計API之路由和方法(採用Restful API規範)：
   - 定義每個資源需要哪些方法：
       - 範例：
          - Users => GET(查), POST(增), PUT(改), PATCH(部分修改), DELETE(刪)
          - Goods => GET(查)
   - 設計URL
      - 對表級別的路由：
         - https://xxx.com/api/{版本號}/{敘述}/{資源}/
             - 版本號：
               - 在維護API過程中，如果不希望影響原有API的操作，此時就可以採用版本控制
               - 因為API一旦釋出上線，要改就不是這麼容易了，也是為了讓使用此API的人能有一個緩衝的時間能去更改程式，所以設置不同的版本
               - 不是每一次改API都需要改版本號，盡量將API可以做成向後相容，這樣就不需要跳版本
               - EX: v1, v2
            - 敘述：
               - 可以用應用名或是其他記號來區別資源
               - 範例: 
                   - https://xxx.com/api/v1/Rank/yr/observations/  =>  年度的排序觀測值
                   - https://xxx.com/api/v1/Rank/mn/observations/  =>  月份的排序觀測值
            - 資源：
               - REST API 是依照「資源」來設計的，而資源是指可由用戶端存取、任何類型的物件、資料或服務
               - 可以讓用戶輕易知道這是什麼
               - EX: goods, orders, observations
            - 範例：
               - https://xxx.com/api/v1/Rank/yr/observations/  =>  排序的年觀測值
               - https://xxx.com/api/v1/orders/  =>  訂單
      - 對紀錄級別的路由：
         - https://xxx.com/api/{版本號}/{敘述}/{資源}/{識別碼(lookup)}/
            - 版本號、敘述、資源 同上
            - 識別碼：
               - 用來識別該資源
               - EX: id, uuid
            - 範例：
               - https://xxx.com/api/v1/users/1/  =>  用戶id為1的那筆紀錄
   - 結合Method和URL
      - REST API 會使用統一的介面，有助於讓用戶端與服務實作分離，並依照不同的HTTP請求(GET、POST、PUT、PATCH和DELETE)做出不同操作
      - 表級別的路由：
         - GET URL：
            - 返回資源列表
            - 範例：
               - GET https://xxx.com/api/v1/users/  =>  返回用戶列表([user1, user2,...])
         - POST URL：
            - 對資源進行新增(Create)操作，並返回新增成功或失敗資訊
            - 範例：
               - POST https://xxx.com/api/v1/users/  =>  新增一個用戶
      - 紀錄級別的路由：
         - GET URL：
            - 返回此資源紀錄(一條紀錄)
            - 範例：
               - GET https://xxx.com/api/v1/users/1/  =>  返回用戶id為1的資訊
         - PUT/PATCH URL：
            - 更新此資源紀錄(一條紀錄)，並返回更新成功或失敗資訊
            - 範例：
               - PUT https://xxx.com/api/v1/users/1/  =>  更新用戶id為1的資料
         - DELETE URL：
            - 刪除此資源紀錄(一條紀錄)，並返回刪除成功或失敗資訊
            - 範例：
               - DELETE https://xxx.com/api/v1/users/1/  =>  刪除用戶id為1的資料
   - 設計權限(如果有需要的話)
      - 認證： 你是誰？
      - 憑證： 使你能行使權限的令牌。
      - 授權： 授予憑證，並可帶著此憑證行使權限。
      - 權限： 你能做什麼？
      - 範例：
            我們登機時會需要機票和護照，
            機票相當於是登上飛機的憑證，也就是說，持有有效的機票就能擁有登機的權利，
            護照或身分證則是為了驗證你的身分，也就是說，當身分驗證成功之後，就能證明你是這張機票的合法持有人且這張機票也會變成有效的憑證，
            最後，你就可以帶著這張機票(憑證)行使登上飛機的權利。
            認證(Authentication)： 驗證護照或身分證
            授權(Authorization)： 給予你能登上飛機的權利
            憑證(Credentials)： 機票
- 使用Swagger工具輔助開發
  - 優點：
     - 通過UI介面可以幫助開發者更易於開發
     - 可以動態產生API接口文檔，減少開發者編寫接口文檔的時間
     - 可以避免改了程式碼，但接口文檔忘了改，解釋不明確帶來歧義的問題發生
  - 缺點：
     - 為了能夠實現自動生成接口文檔，需要在代碼中提前寫大量的註解，生成的接口文檔越清晰，寫的註解越多

## 設計API之返回值格式：
    {
        "status": 狀態碼,
        "errorCode": 錯誤狀態碼,
        "errorMsg": 錯誤詳細敘述,
        "data": 響應數據
    }

## 撰寫文件：
   - 為了讓其他開發者能快速了解API的功能
   - 可以使用Swagger輔助
   - 範例：
      - Request
         - HTTP method 
            - EX: GET, POST等
         - HTTP content-type 
            - EX: application/json等
         - Parameters
            - type: string? number? array? hash?
            - required or optional
      - Response
         - HTTP status code
         - Format
         - Example




