from rest_framework import routers
from .views import (
    BusinessViewSet, BuildingViewSet
)
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'business', BusinessViewSet, basename="business")
router.register(r'buildings', BuildingViewSet, basename="building")
