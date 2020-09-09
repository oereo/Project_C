"""managementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, include
from django.conf import settings

#from rest_framework_simplejwt
#import TokenObtatinPairView, TokenRefreshView
#from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
import mainPage.views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', mainPage.views.home, name="home"),
    #path('data.json', mainPage.views.data_json),
    #
    # path('api/', include("mainPage.urls")),
    # path("api/auth", include("knox.urls")),
    #path("api/", include("user.urls")),
    path("api-auth/", include("rest_framework.urls")),
    #login, registration등 path 설정
    path("api/rest-auth/", include("rest_auth.urls")),
    # 토큰 발급 및 재발급 페이지 설정
    #path('api/rest-auth/obtain_token/', TokenObtatinPairView.as_view(), name="obtain-jwt"),
    #path('api/rest-auth/refresh_token/', TokenRefreshView.as_view(), name="refresh-jwt"),
    #path('api/rest-auth/', include('rest_framework_simplejwt.urls')),

    #path('api/rest-auth/obtain_token/', obtain_jwt_token, name="obtain-jwt"),
    #path('api/rest-auth/refresh_token/', refresh_jwt_token, name="refresh-jwt"),
    path("api/rest-auth/registration/", include("rest_auth.registration.urls")),

]
