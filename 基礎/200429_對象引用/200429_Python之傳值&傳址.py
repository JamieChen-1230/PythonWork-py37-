"""
Python傳參一律是傳『對象引用』，而Python內的數據分為可變與不可變，
當為不可變對象之引用，就相當於為傳值(不能修改原始對象值)，EX：數字、字符串、元組
當為可變對象之引用，就相當於為傳址(或傳引用)(會修改原始對象值)，EX：列表、字典
"""
# 不可變之對象
int_ = 1
float_ = 1.0
str_ = "jamie"
bool_ = True
bytes_ = "a".encode("utf-8")
# 可變之對象
dict_ = {"name": "jamie"}
list_ = [1]


def t(int_, float_, str_, bool_, bytes_, dict_, list_):
    int_ = 100
    float_ = 100.0
    str_ = str_.replace("jamie", "100")
    bool_ = False
    bytes_ = "b".encode("utf-8")
    dict_.setdefault("age", 22)
    list_.append(100)


t(int_, float_, str_, bool_, bytes_, dict_, list_)
# 發現dict和list等可變序列，若在函數內有修改的話，則會影響到原本之序列
print(int_, float_, str_, bool_, bytes_, dict_, list_)


"""
結論：
一、若函數接收到的參數為可變類型，且需要對它進行修改的話，最好先建立該參數之副本，再對副本進行修改。
    原因：因為這樣在函數內修改，才不會影響到函數外部之變量
    解決：先為參數創造副本，再進行操作
"""
