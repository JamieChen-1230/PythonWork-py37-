import requests
from bs4 import BeautifulSoup
from app01 import models
from apscheduler.schedulers.background import BackgroundScheduler


# 創建排程對象
sched = BackgroundScheduler()


def save(dic):
    new_obj = models.News.objects.filter(title=dic.get("title")).first()
    # 資料已存在就不添加
    if new_obj:
        print("資料已存在")
        return
    models.News.objects.create(**dic)


def inner_crawl(url):
    """裡頁面爬蟲"""
    content_res = requests.get(url)
    content_res.encoding = content_res.apparent_encoding
    content_bs = BeautifulSoup(content_res.text, features="lxml")
    # 上傳時間
    info_div = content_bs.find("div", class_="shareBar__info")
    post_date = info_div.find("span").text
    print(post_date)
    return post_date


# 定時行程，12小時運行一次
@sched.scheduled_job('interval', seconds=43200)
def crawler():
    """外頁面爬蟲"""
    response = requests.get(url='https://nba.udn.com/nba/index?gr=www')
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, features="lxml")
    news_body = soup.find("div", id='news_body')
    dt_list = news_body.find_all("dt")
    news_list = []
    for dt in dt_list:
        if dt.attrs.get('class'):
            if "ads" not in dt.attrs.get('class'):
                news_list.append(dt.find('a'))
        else:
            news_list.append(dt.find('a'))

    for new in news_list:
        # 網址
        url = "https://nba.udn.com/" + new.attrs.get('href')
        # print(url)
        # 標題
        title = new.find("h3").text
        print(title)
        # 大綱
        outline = new.find("p").text
        # print(outline)
        post_date = inner_crawl(url)
        # 存進DB
        dic = {
            "title": title,
            "outline": outline,
            "url": url,
            "post_date": post_date,
        }
        save(dic)


def run():
    # li = models.News.objects.all().order_by('-post_date')[:3]
    # message = ''
    # for i in li:
    #     message += i.title + '\n' + i.outline + '\n' + i.post_date + '\n' + i.url + '\n\n'
    # print(message)
    sched.start()

