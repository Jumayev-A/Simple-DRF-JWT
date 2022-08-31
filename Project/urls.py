from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import MyTokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('api/token', MyTokenObtainPairView.as_view()),
    path('api/refresh', TokenRefreshView.as_view())
]

