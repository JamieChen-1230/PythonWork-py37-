from task import add, cmd

# 不是運行add(5, 10) => 這樣只是在本地執行
# 而是要使用 方法名.delay() 這樣才是使用celery分配給worker遠程異步執行
# result = add.delay(5, 10)  # 會返回一個對象
# print(result.get())  # t1.get()返回結果(15)


# 可以一次給多個任務給多個worker執行
# for i in range(3):
#     result = add.delay(4, i)
#     print('第%s個任務: %s+%s=%s' % (i+1, 4, i, result.get()))


result = add.delay(5, 10)  # 會返回一個對象
while not result.ready():  # result.ready()判斷結果否返回了
    print(result.ready())
print(result.get())  # t1.get()返回結果(15)

