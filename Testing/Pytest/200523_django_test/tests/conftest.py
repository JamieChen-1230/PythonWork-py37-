# 鉤子函數：當進行到某個動作時，就會觸發相對應的鉤子函數。
# 讓測試結果可以顯示中文的鉤子函數。
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
所有的测试用例收集完毕后调用, 可以再次过滤或者对它们重新排序
 items （收集的测试项目列表）
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
