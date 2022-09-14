from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('sign-in/', views.SignInView.as_view(), name='sign-in'),
    path('apply/', views.ApplyLogView.as_view(), name='apply'),
    path('logout/', views.logout, name='logout'),
]