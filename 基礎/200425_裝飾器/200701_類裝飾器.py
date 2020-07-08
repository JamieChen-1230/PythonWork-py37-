"""
類裝飾器：
    一、必須實現__call__和__init__兩個方法
        - __init__：接收被裝飾的函數
        - __call__：實現裝飾邏輯
    二、__call__和__init__在類中的作用
        - __init__：初始化實例
        - __call__：使實例能夠像函數一樣被調用，且不會影響到實例的構造
            - 例如: 對象.__call__(*args) 相當於 對象(*args)
"""


import time


class Clock(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        res = self.func(*args, **kwargs)
        end = time.time()
        print('elapse time: ', end-start)
        return res


@Clock
def sneeze(t):
    print('running sneeze....')
    time.sleep(t)


sneeze(3)


class ClockHasParam:
    def __init__(self, fmt="【time: {elapsed}】"):
        self.fmt = fmt

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            end = time.time()
            print(self.fmt.format(elapsed=end-start))
            return res
        return wrapper


@ClockHasParam(fmt="time: __________{elapsed}________")
def sneeze(t):
    print('running sneeze....')
    time.sleep(t)


sneeze(3)
