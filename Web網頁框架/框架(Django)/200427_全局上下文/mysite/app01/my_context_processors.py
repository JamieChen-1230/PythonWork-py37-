"""
要使用這些全局變量，要先定義在settings中的context_processors中。
全局上下文的應用：
    - 通常是用於在多個模版都要使用的數據，EX: 導航列
    - 優點是這樣可以減少重複代碼，且要維護更新時，只要改動這邊即可，不用每個模板都一一去改
"""
from app01 import models


def getData(request):
    # return的資料可以直接在模板中調用
    # {{ user }}  =>  模板中使用
    return {'user': 'jamie'}


def getMenuInfo(request):
    """
    菜單表的所有數據
    """
    menus = models.Menu.objects.all().values('title')
    return {'menu': menus}
