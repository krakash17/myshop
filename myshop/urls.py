
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from storeapp.views import UserViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('storeapp.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('storeapp/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('storeapp/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

