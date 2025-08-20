from rest_framework.routers import DefaultRouter
from .views import VideoPostViewSet

router = DefaultRouter()
router.register(r"videos", VideoPostViewSet)

urlpatterns = router.urls
