from rest_framework import routers
from .views import (
    BusinessViewSet, BuildingViewSet, CommentRUPAPIView,
    CommentsBuildingListAPIView, CommentListViewSet, CommentCreateAPIView
)
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'business', BusinessViewSet, basename="business")
router.register(r'buildings', BuildingViewSet, basename="building")
router.register(r'comments', CommentListViewSet, basename="building-comments")

urlpatterns = router.urls + [
    path('building/<int:pk>/comments', CommentsBuildingListAPIView.as_view(), name="comments-by-build"),
    path('building-comment/<int:pk>', CommentRUPAPIView.as_view(), name="comment-detail"),
    path('building/<int:pk>/comment-create', CommentCreateAPIView.as_view(), name="comment-create")
]
