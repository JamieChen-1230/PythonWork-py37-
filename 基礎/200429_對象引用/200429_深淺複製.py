# ------------淺複製------------(只會創造最外層之容器的副本，適合用在容器內元素皆為不可變之對象時)
# import copy
# l1 = [1, 2]
# l2 = list(l1)  # 使用構造方法做淺複製
# l3 = l1[:]  # 使用切片做淺複製
# l4 = copy.copy(l1)  # 正規用copy()做淺複製
#
# print(l1 == l2)  # => True，==用來比較變量內的值
# print(l1 is l2)  # => False，is用來比較標識
# print(l1 == l3)  # => True，==用來比較變量內的值
# print(l1 is l3)  # => False，is用來比較標識
# print(l1 == l4)  # => True，==用來比較變量內的值
# print(l1 is l4)  # => False，is用來比較標識

# ------------深複製------------(完全複製，副本不共享內部對象之引用)
import copy

class Bus:
    def __init__(self, passenger=None):
        if passenger is not None:
            # self.passenger = passenger  => 要先創造副本，再對副本進行操作
            self.passenger = list(passenger)  # 創造副本並轉換成list
        else:
            self.passenger = []

    def pick(self, name):
        self.passenger.append(name)

    def drop(self, name):
        if self.passenger:
            self.passenger.remove(name)


print("----深淺複製測試----")
bus = Bus(["AA", "BB", "CC"])
bus_shallow = copy.copy(bus)  # 淺複製
bus_deep = copy.deepcopy(bus)  # 深複製

bus.drop("BB")
# 發現bus_shallow會因bus改變而受到影響，bus_deep則不會
print(bus.passenger, bus_shallow.passenger, bus_deep.passenger)
# 通過標識(id)我們也能夠清楚觀察到其中的差異
print(id(bus.passenger), id(bus_shallow.passenger), id(bus_deep.passenger))

print("----可變引用作為參數測試----")
passengers = ["1", "2", "3"]
bus1 = Bus(passengers)
bus2 = Bus(passengers)
bus1.pick("jamie")
print(bus1.passenger, bus2.passenger)


"""
結論：
一、若容器有內包含其他可變類型，請慎用淺複製。
    原因：因為有可能會造成不同的容器，卻在其中共用同一個對象引用
二、不要使用可變類型作為參數默認值。
    原因：因為默認值在模塊加載時就會被定義，所以默認值就會變成該函數對象的屬性，因此有可能會因為不當操作導致默認值被改變
    解決：使用None來代替[]、{}等可變類型作為參數默認值
三、若函數接收到的參數為可變類型，那麼最好是在函數內先創造該參數的副本，再對它進行修改操作。
    原因：因為這樣在函數內修改，才不會影響到函數外部之變量
    解決：先為參數創造副本，再進行操作
"""
