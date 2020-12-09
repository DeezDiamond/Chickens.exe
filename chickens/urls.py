from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChickenViewSet

router = DefaultRouter()
router.register(r'chickens', ChickenViewSet, basename='chicken')
urlpatterns = router.urls