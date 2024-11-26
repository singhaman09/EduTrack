"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from students.views import login_view  # Import login_view explicitly

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('', login_view, name='login'),  # Root URL for login page
    path('students/', include('students.urls')),  # Include student app URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT Token API
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh API
]
