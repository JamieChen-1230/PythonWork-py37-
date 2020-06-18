<<<<<<< HEAD
# nice to meet you
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。  完成
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。  完成
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表  完成
	 * 新聞詳情頁面  完成
4. 以 Pull-Request 的方式將代碼提交。  完成
	
## 進階要求
1. 使用 Scrapy。  完成
2. 實現爬蟲自動定時抓取。  完成(是用bs4做的)
3. 使用 Websocket 服務，抓取到新的新聞時立即通知前端頁面。  完成(但有bug，重新整理頁面後失效)
4. 将本 demo 部署至服务器并可正确运行。
=======
# nice to meet you project
## 測試網址：
https://djangobyjamie.herokuapp.com/  
## 完成要求：
#### 基本：
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB(sqlite)。
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面
4. 以 Pull-Request 的方式將代碼提交。
#### 進階：
1. 使用 Scrapy。
```python
# 在myscrapy中
```
2. 實現爬蟲自動定時抓取。  (使用apscheduler實現。)
```python
# 在nba/nba_crawler.py中
from apscheduler.scheduler import Scheduler
sched = Scheduler()
sched.add_interval_job(crawler, seconds=60, args=[request])
sched.start()
```
3. 使用 Websocket 服務，抓取到新的新聞時立即通知前端頁面。 (但有bug，重新整理頁面後會失效，所以佈署到Heroku的版本沒有使用。)
```python
# 在nba/views.py中
@accept_websocket
def websocket_msg(request):
    if not request.is_websocket():  # 判断是不是websocket连接
        # 如果是普通的http方法
        return render(request, 'index.html')
    else:
        # 透過bs4實現定時爬蟲，且有更新時提醒前端
        nba_crawler.main(request)
        for message in request.websocket:
            request.websocket.send(message)  # 發送信息到前端
```
4. 将本 demo 部署至服务器并可正确运行。  
```python
# 佈署到Heroku中
```


## 未完成要求：
>>>>>>> e51b9d289f715d3f18dd9ecdf6cd42bb4f2474b4
5. 所實現新聞列表 API 可承受 100 QPS 的壓力測試。

## 開發環境(windows)：
python==3.5.1  
Django==1.11.6  
djangorestframework==3.5.1  
dwebsocket==0.5.12  
Scrapy==1.6.0  
APScheduler==2.1.2  
requests==2.23.0  
beautifulsoup4==4.9.0  
Twisted==18.9.0  


