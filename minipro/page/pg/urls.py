from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index, name="index"),
    path('main1', views.main1, name="main1"),
    path('main4', views.main4, name="main4"),
]