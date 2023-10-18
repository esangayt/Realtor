
from django.contrib import admin
from django.urls import path, include

from userApp.api.views import (
    logout_view, registration_view, login_view
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView, TokenBlacklistView,
)

urlpatterns = [
    path('logout/', logout_view, name="logout"),
    path('register/', registration_view, name="register"),
    path('login/', login_view, name="login"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
