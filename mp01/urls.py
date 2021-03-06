"""mp01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from mp01 import views

urlpatterns = [
    path('admin/', admin.site.urls),                    # 관리자 페이지
    path('', views.HomeView.as_view(), name='home'),    # 첫 페이지
    path('country/', include('country.urls')),          # 국가별, 대륙별 앱
    path('member/', include('member.urls')),            # 회원가입 관련 앱
    path('magazine/', include('magazine.urls')),        # 매거진 앱
    path('board/', include('board.urls')),              # 게시판 앱
    path('aboutUs', TemplateView.as_view(template_name='aboutUs.html')),   # 어바웃 어스
]