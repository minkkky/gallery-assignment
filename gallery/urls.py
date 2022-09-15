from django.urls import path
from . import views

app_name = "gallery"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("art/", views.ArtView.as_view(), name="art"),
    path("artist/", views.ArtistListView.as_view(), name="artist"),
    path("exbihition/", views.ExbihitionView.as_view(), name="exbihition"),
]