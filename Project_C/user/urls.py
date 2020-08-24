from django.urls import path
from user.views import CurrentUserAPIView

urlpatterns = [
    path("user/", CurrentUserAPIView.as_view(), name="current-user"),
]