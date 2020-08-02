from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', viewset=views.UsersViewSet)


urlpatterns = router.urls
