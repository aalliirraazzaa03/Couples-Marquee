"""
URL configuration for couples_maquree project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_login'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # password reset
    # path('api/auth/password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path(
    #     'api/auth/password-reset-confirm/<uidb64>/<token>/',
    #     auth_views.PasswordResetConfirmView.as_view(),
    #     name='password_reset_confirm'
    # ),



    # Common base for all APIs
    path('api/events/', include('Events.urls')),
    path('api/decor/', include('Decor.urls')),
    path('api/payments/', include('Payments.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)