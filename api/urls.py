from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, LocationViewSet, ResourceViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'resources', ResourceViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
