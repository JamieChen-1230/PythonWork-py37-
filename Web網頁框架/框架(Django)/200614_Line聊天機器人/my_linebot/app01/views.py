from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from app01 import nba_crawler
from app01 import models

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

import configparser
# 從config.ini檔中讀取資料
config = configparser.ConfigParser()
config.read('config.ini')

# LineBot連結時所需的密碼和權杖，這裡是存在config.ini裡
LINE_CHANNEL_ACCESS_TOKEN = config.get('line-bot', 'channel_access_token')
LINE_CHANNEL_SECRET = config.get('line-bot', 'channel_secret')

# line_bot_api 負責與Line本身的API接口做溝通
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
# handler 負責處理送過來的資料
handler = WebhookHandler(LINE_CHANNEL_SECRET)

nba_crawler.run()


# @csrf_exempt可以讓此方法免除crsf認證
@csrf_exempt
def callback(request):
    # Line用戶端傳來的消息為POST請求
    if request.method == 'POST':
        # 為了要確認此request是不是從line server傳過來的，
        # 所以我們去抓取request的header和body
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            # handler會判斷這個訊息類型應該被哪個處理器處理，就會傳給那個函數處理
            handler.handle(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        return HttpResponse('OK')
    else:
        return HttpResponse('OK')


# 處理文字訊息的handler：當收到MessageEvent(信息事件)，且信息是屬於TextMessage(文字信息)時，此函數會被調用
@handler.add(MessageEvent, message=TextMessage)
def text_message(event):
    """
    line_bot_api.reply_message(reply_token, 要執行的動作)
    reply_token：只能使用一次，用完即丟。
    """
    if '焦點' in event.message.text:
        li = models.News.objects.all().order_by('-post_date')[:3]
        message = ''
        for i in li:
            message += i.title + '\n' + i.outline + '\n' + i.post_date + '\n' + i.url + '\n'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=message))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))
