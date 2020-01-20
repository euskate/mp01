from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'(?P<code>[A-Z]{2})/', views.country, name='country'),   # 나라별 페이지
    path('continent', views.continent, name="continent"),           # 대륙별 페이지
    path('top', views.top, name="top"),           # 
]