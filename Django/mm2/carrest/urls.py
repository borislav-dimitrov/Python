from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.views import CustomTokenObtainPairView

urlpatterns = [
    path('api-token-auth/', CustomTokenObtainPairView.as_view()),
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
    path('', include('car.urls')),
    path('ad/', include('carAd.urls')),
    path('api/', include('user.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
