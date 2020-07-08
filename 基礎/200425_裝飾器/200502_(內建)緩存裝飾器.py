"""
functools.lru_cache是標準庫中提供的裝飾器：
    用途：提供了緩存功能，可避免傳入相同的參數時造成重複計算、資源浪費。
    可選參數：
        maxsize：指定能儲存多少個緩存結果，當緩存滿時，會刪除最舊的一個結果。（應設為2的次冪）
        typed：若設為True，會把不同類型參數得到的結果分開存。（f(3)和f(3.0)就會分開存）
    注意：被裝飾的函數的參數必須皆為可散列的（EX：str、bytes、frozenset、數值類型、皆為可散列組成的元組等）。
"""
import time
import functools


# 顯示結果裝飾器
def check(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(0.1)
        res = func(*args, **kwargs)
        print("{time}  {name}({parameter}) -> {result}".format(time=time.time()-start,
                                                               name=func.__name__,
                                                               parameter=", ".join(repr(arg) for arg in args),
                                                               result=res))
        return res
    return wrapper


# ---------無使用緩存---------
# 費波納西數列
@check
def fibonacci(n):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return n


print(fibonacci(6))
print("------------------------------------------------")


# ---------有使用緩存---------
# 費波納西數列
@functools.lru_cache(maxsize=128, typed=False)
@check
def fibonacci(n):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return n


print(fibonacci(6))
