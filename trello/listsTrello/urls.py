from rest_framework.routers import DefaultRouter
from .views import ListsTrelloViewSet


router = DefaultRouter()
router.register(r"lists", ListsTrelloViewSet, basename="lists")
urlpatterns = router.urls
