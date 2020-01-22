from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index, name="index"),
    path('main1', views.main1, name="main1"),
    path('main2', views.main2, name="main2"),
    path('main3', views.main3, name="main3"),
]