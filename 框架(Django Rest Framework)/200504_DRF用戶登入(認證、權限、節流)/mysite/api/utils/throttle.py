# ※ 源碼中已經有實現比我們更好的訪問節流器，所以使用繼承他的就好
#
# from rest_framework.throttling import BaseThrottle
# import time
# VISIT_RECORD = {}  # 只是因為測試才這樣使用，實際開發應該放到緩存或資料庫
# class VisitThrottle(BaseThrottle):
#     """
#     10秒內只能訪問3次
#     """
#     def __init__(self):
#         self.history = None
#     # 判斷是否可以繼續訪問
#     def allow_request(self, request, view):
#         # 1.獲取用戶IP
#         remote_addr = request.META.get('REMOTE_ADDR')
#         ctime = time.time()
#         if remote_addr not in VISIT_RECORD:
#             # 沒有訪問紀錄者
#             VISIT_RECORD.setdefault(remote_addr, [ctime, ])
#             return True
#         self.history = VISIT_RECORD.get(remote_addr)
#         # 刪除超過10秒以上的訪問紀錄
#         while self.history and (self.history[-1] < ctime - 10):
#             self.history.pop()
#
#         if len(self.history) < 3:
#             # 把最新的時間放在最前面
#             self.history.insert(0, ctime)
#             return True
#
#         # return True => 表示可以繼續訪問
#         # return False => 表示訪問頻率太高，不可繼續訪問
#         return False
#     def wait(self):
#         """
#         :return: 還需要等多少秒
#         """
#         ctime = time.time()
#         return 10 - (ctime - self.history[-1])

from rest_framework.throttling import SimpleRateThrottle


# SimpleRateThrottle的歷史紀錄是存在Django中的內置緩存裡
class VisitThrottle(SimpleRateThrottle):  # 只要實現這樣就能得到一個訪問節流器了
    # 作為key，到時要到settings.py裡取我們設定的頻率
    scope = 'ip'

    # get_cache_key表示訪問紀錄的key，這要我們自己覆寫
    def get_cache_key(self, request, view):
        # 使用用戶IP當作key
        return self.get_ident(request)  # 父類的get_ident(request)方法可以直接取IP


class UserVisitThrottle(SimpleRateThrottle):  # 只要實現這樣就能得到一個訪問節流器了
    # 作為key，到時要到settings.py裡取我們設定的頻率
    scope = 'username'

    # get_cache_key表示訪問紀錄的key，這要我們自己覆寫
    def get_cache_key(self, request, view):
        # 使用用戶名當作key
        return request.user.username
