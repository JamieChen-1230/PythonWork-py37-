"""
Python的作用域（Scope）規則：
        一、Scope在查找時是按照LEGB做查找：Local -> Enclosed -> Global -> Built-in
                    Local：於function或是class內宣告的變數名
                    Enclosed：位於巢狀層次的function結構，常用於Closure
                    Global：最上層位於模組(module)的全域變數名稱
                    Build-in：內建模組(module)的名稱，例如print, abs()這樣的函式等等
"""


# -----------global(全域)變數-----------
# 放在function外的變數
global_a = "hello global_a"

def scope_1():
    print(global_a)

scope_1()


# -----------local(區域)變數-----------
# function內執行的區域稱作「local scope」，而建立區域變數最簡單的方式是於function中給定一個變數。
# 一般來說，全域變數是無法被該function scope內重新定義的變數進行存取。
b = "hello b"
def scope1():
    b = 1

scope1()
print(b)  # => b

# 若要讓local scope內的變數讓外部進行存取，可以在目標變數的前面宣告一個global。
c = "hello c"
def scope1():
    global c
    c = 1

scope1()
print(c)  # => 1


# -----------Enclosed Scope-----------
# 依據巢狀層次從內到外搜尋，Python會從最近的enclosing scope向外找起，enclosing scopes裡的變數，稱作non-local variable。
def outer(a):
    b = a

    def inner():
        c = 3

        def inner_inner(b):
            k = b+c
            return b+c
        return inner_inner
    return inner


outcome = outer(5)
ans = outcome()
# 以上述範例來說，b是outer()的區域變數，c是inner()的區域變數，由於離inner()最近的scope是outer所建立的，b又是於此scope被宣告，所以b是inner()的non-local variable。
# 而以inner_inner()來看，k為它的區域變數 ，值為b+c，這時的b並非被宣告在outer()的scope裡，而是藉由參數傳遞的，也就是說，b屬於local variable。
# 反之c則是被宣告在inner()的scope裡，對inner_inner()來說，是屬於non-local variable。
print(ans(3))  # => 6
