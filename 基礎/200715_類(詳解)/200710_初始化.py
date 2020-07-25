# ===========-執行順序-===========
class A(object):
    """
        __new__方法：
            - 在Python中是真正的構造方法（建立並返回對象），通過這個方法可以產生一個與類(cls)對應的實例對象。
            - 始終都是類的靜態方法（即第一個引數為cls），即使沒有被加上靜態方法裝飾器。
        __init__方法：
            - 是一個初始化的方法，並將對這個物件進行相應的初始化操作(self代表由類產生出來的實例對象)。
    """
    def __init__(self, *args, **kwargs):  # 後執行(初始化對象)
        print("init %s" % self.__class__)

    def __new__(cls, *args, **kwargs):  # 先執行(建立對象)
        print("new %s" % cls)
        # super(<類名>, <對象(self)或類(cls)>)
        return super(A, cls).__new__(cls, *args, **kwargs)
        # return object.__new__(cls, *args, **kwargs)

# a = A()


# ===========-new方法決定了是否要執行init方法-===========
class B(object):
    def __init__(self, *args, **kwargs):
        print("Call __init__ from %s" % self.__class__)
        self.b1 = "b1"

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls, *args, **kwargs)
        print("Call __new__ for %s" % obj.__class__)
        return obj


class C(object):
    """
    如果__new__方法沒有返回obj(即「當前類」的對象)，那麼當前類的__init__方法是不會被呼叫的。
    """
    def __init__(self, *args, **kwargs):
        print("Call __init__ from %s" % self.__class__)
        self.c1 = "c1"

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(B, *args, **kwargs)
        print("Call __new__ for %s" % obj.__class__)
        return obj

# c = C()
# print(type(c))


# ===========-派生不可變型別-===========
class Round2Float(float):
    def __new__(cls, num):
        num = round(num, 2)
        return float.__new__(Round2Float, num)

f = Round2Float(4.14159)
print(f)
