from django.urls import path

from . import views

urlpatterns = [
    path('arts/', views.ArtListView.as_view(), name='art-list'),
    path('exbihitions/', views.ExbihitionListView.as_view(), name='exbihition-list'),
    path('artists/', views.ArtistListView.as_view(), name='artist-list'),
]