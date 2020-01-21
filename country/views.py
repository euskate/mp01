from django.shortcuts import render
from .models import CountryName, TravelByCountry
# Create your views here.

# 국가별로 그래프를 보여주는 뷰
def country(request, code):
    try:
        # 국가명을 국가코드에서 가져온다.
        countryName = CountryName.objects.get(code=code)
    
        yearData = [ i for i in range(2000,2020) ]
        print(yearData)
        # 빈 리스트에 일치하는 국가명의 DB를 가져온다.
        countryData = list()
        obj = TravelByCountry.objects.get(country=countryName)
        
        # 리스트에 DB의 연도별 data를 담는다.
        countryData.append(obj.y2000)
        countryData.append(obj.y2001)
        countryData.append(obj.y2002)
        countryData.append(obj.y2003)
        countryData.append(obj.y2004)
        countryData.append(obj.y2005)
        countryData.append(obj.y2006)
        countryData.append(obj.y2007)
        countryData.append(obj.y2008)
        countryData.append(obj.y2009)
        countryData.append(obj.y2010)
        countryData.append(obj.y2011)
        countryData.append(obj.y2012)
        countryData.append(obj.y2013)
        countryData.append(obj.y2014)
        countryData.append(obj.y2015)
        countryData.append(obj.y2016)
        countryData.append(obj.y2017)
        countryData.append(obj.y2018)
        countryData.append(obj.y2019)

        # 확인용(콘솔)
        print(countryData)

    # 국가명이 없을 경우 국가명 변수에 None을 담는다.
    except Exception as e:
        countryName = None
        countryData = None
        yearData = None

    return render(request, 'country/country.html', {'countryName':countryName, 'countryData':countryData, 'yearData':yearData})

# 대륙별로 그래프를 보여주는 뷰
def continent(request, code):
    return render(request, 'country/continent.html', {'code':code})

# 순위를 보여주는 뷰
def top(request):
    return render(request, 'country/top.html')