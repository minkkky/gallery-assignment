from django.urls import path
from . import views

app_name = "artist"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signin/", views.SignInView.as_view(), name="signin"),
    path("application/", views.ArtistView.as_view(), name="application"),
    path("dashboard/", views.DashboardView.as_view(), name="info"),
    path("regist/art/", views.ArtPostView.as_view(), name="art"),
    path("regist/exbihition/", views.ExbihionPostView.as_view(), name="exbihition"),
]