from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# basename: url的別名，默認會自動去視圖(viewset)中的queryset屬性抓取(所以如果視圖中沒設置queryset屬性，就必須要設置basename)
router.register(r'roles', viewset=views.RolesViewSet, basename="role")
router.register(r'permissions', viewset=views.PermissionsViewSet, basename="permission")
router.register(r'users', viewset=views.UsersViewSet, basename="user")


urlpatterns = router.urls
