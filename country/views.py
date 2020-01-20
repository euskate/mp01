from django.shortcuts import render
from .models import CountryName
# Create your views here.

def country(request, code):
    # 국가명을 국가코드에서 가져온다.
    try:
        contryName = CountryName.objects.get(code=code)
    # 국가명이 없을 경우 국가명 변수에 None을 담는다.
    except Exception as e:
        contryName = None
    
    return render(request, 'country/country.html', {'countryName':contryName})

def continent(request, code):
    return render(request, 'country/continent.html', {'code':code})

def top(request):
    return render(request, 'country/top.html')