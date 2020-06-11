class Taiwanese:
    # 類屬性
    species = "people"
    country = "TW"

    def __init__(self, name, sex):
        # 實例屬性
        self.name = name
        self.sex = sex

    # 普通方法
    def walk(self):
        print("%s is walking" % self.name)

    # 靜態屬性
    @property
    def talk(self):
        print("%s is talking" % self.name)

    # 類方法
    # 這樣的方法第一個參數永遠綁定為類別物件本身(cls)，無論是以實例方法來呼叫，或是以靜態方法來呼叫
    @classmethod
    def born(cls):
        # cls.my_sum(1, 3)
        print("I born in %s" % cls.country)

    # 靜態方法
    # 如果你在定義類別時，希望某個方法不要作為實例的綁定方法，也就是不要將第一個參數綁定為self
    @staticmethod
    def my_sum(x, y):
        print(x + y)


# 類屬性 => 為共享屬性，類與實例皆可調用
# p1 = Taiwanese("Jamie", "男")
# p2 = Taiwanese("Candy", "女")
# Taiwanese.country = "CN"  # 類屬性是被所有實例所共享
# p1.country = "P1COUNTRY"  # 這樣p1會設置一個country實例屬性，所以之後被調用的話會優先顯示實例屬性而不是類屬性
# print(p1.__dict__)
# print(p2.__dict__)
# print(Taiwanese.__dict__)
# print(p1.country, p2.country)
# print(Taiwanese.country)


# 實例屬性 => 各自實例互相獨立，僅實例可調用
# p1 = Taiwanese("Jamie", "男")
# p2 = Taiwanese("Candy", "女")
# p1.name = "Jamie2"
# print(p1.name, p2.name)
# # print(Taiwanese.name)  # => 報錯(AttributeError: type object 'Taiwanese' has no attribute 'name')


# 普通方法 => 共享，僅實例可調用
# p1 = Taiwanese("Jamie", "男")
# p2 = Taiwanese("Candy", "女")
# def walk(self):
#     print("%s is walking too" % self.name)
# Taiwanese.walk = walk
# p1.walk()
# p2.walk()
# # Taiwanese.walk()  # 報錯，因為只有實例可以調用


# 靜態屬性 => 共享，僅實例可調用
# p1 = Taiwanese("Jamie", "男")
# p2 = Taiwanese("Candy", "女")
# @property
# def talk(self):
#     print("%s is talking too" % self.name)
# Taiwanese.talk = talk
# p1.talk
# p2.talk
# # Taiwanese.talk  # 不會報錯但也不會有任何顯示，因為只有實例可以調用


# 類方法 => 共享，類與實例皆可調用
# p1 = Taiwanese("Jamie", "男")
# p2 = Taiwanese("Candy", "女")
# @classmethod
# def born(cls):
#     print("I born in %s too" % cls.country)
# Taiwanese.born = born
# p1.born()
# p2.born()
# Taiwanese.born()


# 靜態方法 => 共享，類與實例皆可調用
# p1 = Taiwanese("Jamie", "男")
# p2 = Taiwanese("Candy", "女")
# @staticmethod
# def my_sum(x, y):
#     print(x + y + 1)
# Taiwanese.my_sum = my_sum
# p1.my_sum(1, 1)
# p2.my_sum(1, 1)
# Taiwanese.my_sum(1, 1)


# ----------------- 繼承 -----------------
# class Taiwanese2(Taiwanese):
#     pass
# t1 = Taiwanese2('jamie2', 888)
# t1.my_sum(100, 200)  # OK(子類對象調用父類的靜態方法)
# Taiwanese2.my_sum(111, 222)  # OK(子類調用父類的靜態方法)
# t1.born()  # OK(子類對象調用父類的類方法)
# Taiwanese2.born()  # OK(子類調用父類的類方法)
# t1.talk  # OK(子類對象調用父類的靜態屬性)
# t1.walk()   # OK(子類對象調用父類的實例方法)


# ----------------- 繼承加覆寫 -----------------
# class Taiwanese3(Taiwanese):
#     def walk(self):
#         print("%s is walking in Taiwanese3" % self.name)
#
#     @property
#     def talk(self):
#         print("%s is talking in Taiwanese3" % self.name)
#
#     @classmethod
#     def born(cls):
#         print("I born in %s in Taiwanese3" % cls.country)
#
#     @staticmethod
#     def my_sum(x, y):
#         print(x + y + 333)
#
#
# t1 = Taiwanese3('jamie3', 333)
# t1.walk()  # OK(子類可覆寫父類的實例方法)
# t1.talk  # OK(子類可覆寫父類的靜態屬性)
# t1.born()  # OK(子類可覆寫父類的類方法)
# Taiwanese3.born()
# t1.my_sum(1, 1)   # OK(子類可覆寫父類的靜態方法)
# Taiwanese3.my_sum(1, 1)
