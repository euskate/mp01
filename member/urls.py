from django.urls import path
from . import views

# 127.0.0.1:8000/member/index  => index 함수 동작
# 127.0.0.1:8000/member/join  => join 함수 동작
# 127.0.0.1:8000/member/login  => login 함수 동작

urlpatterns = [
    path('auth_join', views.auth_join, name="auth_join"),
    path('auth_index', views.auth_index, name="auth_index"),
    path('auth_edit', views.auth_edit, name="auth_edit"),
    path('auth_login', views.auth_login, name="auth_login"),
    path('auth_logout', views.auth_logout, name="auth_logout"),
    path('auth_pw', views.auth_pw, name="auth_pw"),
]