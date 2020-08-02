from rest_framework.permissions import BasePermission
from django.forms.models import model_to_dict


class MyPermission(BasePermission):
    # message表示未通過權限的顯示訊息
    message = '權限不足'

    def has_permission(self, request, view):
        """
        Description:
            一、對於「表」級別的權限設置
            二、先執行has_permission()，再執行has_object_permission()
            三、當在has_permission()中為False的話，就不會運行has_object_permission()
        Parameters:
            request: 經過DRF再包裝的request，包含Django原本的request功能
            view: 可通過它調用視圖相關參數
        return:
            bool: True為通過驗證；False為驗證失敗
        """
        role_list = request.user.roles.all()
        for role in role_list:
            for pm in role.permissions.all():
                if pm.resource == view.basename and pm.method == view.action:
                    return True  # True 代表有權訪問

        if request.user.is_superuser:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        """
        Description:
            一、對於「紀錄」級別的權限設置
            二、先執行has_permission()，再執行has_object_permission()
            三、當在has_permission()中為False的話，就不會運行has_object_permission()
        Parameters:
            request: 經過DRF再包裝的request，包含Django原本的request功能
            view: 可通過它調用視圖相關參數
            obj: 要執行操作的model實例對象
        return:
            bool: True為通過驗證；False為驗證失敗
        """
        print(view.action)
        print(model_to_dict(obj))
        if view.action == 'retrieve':
            self.message = '權限不足，只能查看自己的user資料'
            return obj == request.user or request.user.is_superuser
        elif view.action == 'destroy':
            self.message = '權限不足，只有superuser能刪除用戶'
            return request.user.is_superuser
        return True


