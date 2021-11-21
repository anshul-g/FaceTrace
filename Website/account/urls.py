from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name = ""),
    path('logout/', views.logout_request, name= ""),
]