from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'(?P<code>[A-Z]{2})/', views.country, name='country'),   # 나라별 페이지
    re_path(r'^top/(?P<year>[0-9]{0,4})', views.top, name="top"),           # 
    re_path(r'(?P<cont>[a-z]{4,10})/', views.continent, name="continent"),           # 대륙별 페이지
    path('vote', views.vote, name="vote"),
]