from django.conf.urls import url
from django.urls import path, include
from mainPage import views

urlpatterns = [
    path('index', views.index, name ="index"),
    path('dashboard/', views.dashboard, name ="dashboard"),
    path('icons/', views.icons, name ="icons"),
    path('', views.loginp, name ="login"),
    path('map/', views.map, name ="map"),
    path('maps/', views.maps, name ="maps"),
    path('profile/', views.profile, name ="profile"),
    path('register/', views.register, name ="register"),
    path('tables/', views.tables, name ="tables"),
    path('upgrade/', views.upgrade, name ="upgrade"),
    path('login_user/', views.login_user, name ="login_user"),

]