from django.urls import path
from . import views

app_name = "tool"

urlpatterns = [
path("admintool/", views.IndexView.as_view(), name="index"),
path("statistics/", views.StatisticsView.as_view(), name="statistics"),
path("regist/", views.RegistrationView.as_view(), name="regist"),
]