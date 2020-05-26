from rest_framework.permissions import BasePermission


class SVIPPermission(BasePermission):
    # message:表示未通過權限的顯示訊息。(一定要使用message)
    message = '必須是SVIP才能訪問'

    def has_permission(self, request, view):
        if request._request.user.user_type != 3:
            return False
        return True  # 表有權訪問


class OtherPermission(BasePermission):
    # message:表示未通過權限的顯示訊息。(一定要使用message)
    message = '必須是普通用戶或VIP才能訪問'

    def has_permission(self, request, view):
        if request._request.user.user_type == 3:
            return False
        return True  # 表有權訪問
