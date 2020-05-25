class BlackMedium:
    feature = "Ugly"

    def __init__(self, name, addr,):
        self.name = name
        self.addr = addr

    def sell_house(self):
        print('%s 正在賣房子' % self.name)

    def rent_house(self):
        print("%s 正在租房子" % self.name)


b1 = BlackMedium("SB仲介", "台北")


# -------內置函數-------
# isinstance() 判斷對象是否屬於這個類
# print(isinstance(b1, BlackMedium))  # => True

# issubclass() 判斷是否為子類
# class Foo(BlackMedium):
#     pass
# f1 = Foo("SB仲介", "台北")
# print(issubclass(Foo, BlackMedium))  # => True
# print(isinstance(f1, BlackMedium))  # => True，繼承過來的也可以

# hasattr() 判斷object能不能調用相對應的屬性或方法(而不是本身有沒有這個屬性或方法)
# print(hasattr(b1, 'name'))  # => True
# print(hasattr(b1, 'sell_house'))  # => True
# print(hasattr(BlackMedium, "feature"))  # => True，類也能使用(因為類本身也是一種對象)

# getattr() 找出object中相對應的屬性和方法，默認找不到則報錯，若有設default則顯示default文字
# print(getattr(b1, 'name'))  # => SB仲介，等同於b1.name
# print(getattr(b1, 'sell_house'))
# # => <bound method BlackMedium.sell_house of <__main__.BlackMedium object at 0x0000019E53CA9D30>>
# func = getattr(b1, 'sell_house')
# func()
# # print(getattr(b1, 'sell_hou'))  # => error
# print(getattr(b1, 'sell_hou', '找不到相關方法'))  # => 找不到相關方法

# setattr() 若無該屬性則新增，有則修改
# setattr(b1, 'Sb', True)  # 等同於b1.Sb = True
# print(b1.__dict__)
# setattr(b1, 'name', "SSSSSSB仲介")
# print(b1.__dict__)
# setattr(b1, 'func', lambda x: x+1)
# print(b1.__dict__)
# print(b1.func(10))

# delattr() 刪除屬性
# delattr(b1, 'name')  # 等同於del b1.name
# print(b1.__dict__)

# -------反射-------
# 當某個類為定義完成時，能先定義好實例接口，類的方法能晚點補上(很適用於兩個不同工程師使用，不會影響對方的進度)
# class Ftp:
#     def __init__(self, addr):
#         self.addr = addr
#
#
# f1 = Ftp('1.1.1.1')
# # f1.put()  # => error，不能這麼寫會報錯
# # 可插拔之設計
# if hasattr(f1, "put"):
#     func = getattr(f1, 'put')
#     func()
# else:
#     print('put未完成')

