"""
閉包(Closure)：
    假設有個巢狀函式，最外層的函式把自己內層嵌套另外一個函式，將這個嵌套的函式作為回傳值傳遞出去，便會形成一個Closure。
"""


def student():
    height = 170
    weight = 60

    def info():
        print("my height is {}.".format(height))
        print("my weight is {}.".format(weight))
    return info


print(student)
print(student())
# 一般情況下，function中內區域變數會隨著function執行完畢而結束。
# 而至於height、weight能被讀取，是在於return info這，info函數趁著return的時候捕捉外層函式裡的變數，並偷渡進來自己的scope裡面。
# 被捕捉的變數便稱做【captured variable】，帶有captured variable的函式稱為【closure】。
s = student()
s()


# -----------對Captured variables重新賦值-----------
def student():
    height = 170
    weight = 60

    def info():
        # 在function scope中，當變數被賦值時，Python會自動將變數設定為區域變數。
        # 但在info中卻找不到height、weight等區域變數，因此會報錯。
        # captured variable在Python中並非區域或全域變數，所以只能用nonlocal去宣告變數，才能進行修改操作。
        nonlocal height
        nonlocal weight
        height += 1
        weight += 1
        print("my height is {}.".format(height))
        print("my weight is {}.".format(weight))
    return info


s = student()
s()
