from django.shortcuts import render, redirect, get_object_or_404
from .models import CountryName, ContinentName, TravelByCountry
# Create your views here.


import numpy as np
import pandas as pd
import seaborn as sns
from base64 import b64encode 
import cx_Oracle as oci

from django.db.models import Sum, Max, Min, Count, Avg
import pandas as pd #conda install pandas
import matplotlib.pyplot as plt
import io # byte로 변환
import base64 # byte를 base64로 변경
from matplotlib import font_manager, rc #한글 폰트 적용



# 순위를 보여주는 뷰
def top(request, year="2010"):
    try:
        yearData = [ i for i in range(2000,2020) ]  # 2000 ~ 2019
        yearStr = 'y' + year
        yearStrDesc = '-y' + year

        # print(yearStr)
        # 연도별로 위에서부터 3개만 가져 옴
        obj = TravelByCountry.objects.all().order_by(yearStrDesc)[1:6]


        # print(obj.__dict__)
            # 가져온 data를 딕셔너리로 만든다.
        # for key, value in obj.__dict__.items():
        #     # 해당연도 데이터만 가져와서 변수에 담는다.
        #     print(key, value)
        #     # if 'y' == key[0] :
        #     #     countryData.append(value)

        labels = list()
        data = list()
        
        # 콘솔에서 확인
        for row in obj.values(yearStr):
            # print(row[yearStr])
            data.append(row[yearStr])
        for row in obj.values('country'):
            # print(row)
            labels.append(row['country'])
        
        # print(labels)
        # print(data)

        # 역순 바꾸기
        labels.reverse()
        data.reverse()
        # data /= 1000
        # print(data)

        # labels 변수 : top 3 국가명 (막대 그래프 y축의 라벨명)
        # data 변수 : 여행객 수 (막대 그래프의 길이)

        # 여기 아래에다가 차트 구현을 해서 템플릿으로 넘겨 봅시다. (템플릿은 /template/country/top.html에 있음.)

        ### 한글 적용  ###
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font', family=font_name)
        ### 한글 적용 ###

        # 차트 크기 지정
        plt.figure(figsize=(7,5))
        colors = ['salmon', 'orange', 'cadetblue', 'skyblue', 'coral']

        num_bars = len(data)
        positions = range(1, num_bars + 1)


        plt.barh(positions, data, align='center', color=colors, label=labels)
        
        for i, v in enumerate(data):
            plt.text(v, i + 0.9, str(v),)
        
        
        plt.yticks(positions, labels)
        plt.xlabel('여행객')
        plt.ylabel('국가')
        plt.title(year+'년도 Top 5')
        plt.grid()
        # plt.draw()


        avg_img = io.BytesIO()    # img에 byte 배열로 보관
        plt.savefig(avg_img, format="png")  # png파일 포맷으로 저장
        avg_img_url = base64.b64encode(avg_img.getvalue()).decode()

        plt.close()
        
        context = {'yearData':yearData, 'graph1':'data:;base64,{}'.format(avg_img_url), }
    except Exception as e:
        return redirect('/country/top/2000')
    return render(request, 'country/top.html', context)

# 대륙별로 그래프를 보여주는 뷰
def continent(request, cont):
    contName = get_object_or_404(ContinentName, cont=cont)
    yearData = [ str(i) for i in range(2000,2020) ]  # 2000 ~ 2019

    obj = TravelByCountry.objects.filter(continent__contains=str(contName))
    cont_kr = ContinentName.objects.filter(cont__contains=str(contName)).values('c_name')[0]['c_name']
    

    ### 한글 적용  ###
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
    ### 한글 적용 ###
    
    # print(obj)

    coun = list()
    data = list()
    
    # 차트 크기 지정
    plt.figure(figsize=(12,8))
    
    for row in obj:
        data = list()
        # 가져온 data를 딕셔너리로 만든다.
        # print(row.country)
        for key, value in row.__dict__.items():
            # 해당연도 데이터만 가져와서 변수에 담는다.
            # print(key, value)
            if 'y' == key[0] :
                data.append(value)
        plt.plot( yearData, data, label=row.country )
        plt.legend(loc='best')
        
    
    # # 콘솔에서 확인
    # for row in obj.values(yearStr):
    #     # print(row[yearStr])
    #     data.append(row[yearStr])
    # for row in obj.values('country'):
    #     print(row)
    #     coun.append(row['country'])
    # for i in obj:
    #     print(i)

    
    plt.xlabel('년도')
    plt.ylabel('여행객')
    plt.title(cont_kr+' 대륙의 연도별 여행객 수')
    
    plt.grid()
    # plt.draw()

    avg_img = io.BytesIO()    # img에 byte 배열로 보관
    plt.savefig(avg_img, format="png")  # png파일 포맷으로 저장
    avg_img_url = base64.b64encode(avg_img.getvalue()).decode()

    plt.close()

    context = {
        'yearData':yearData, 
        'cont':contName, 
        'obj':obj,
        'graph1':'data:;base64,{}'.format(avg_img_url) }

    return render(request, 'country/continent.html', context )


def vote(request):
    if request.method == 'POST':
        # try:
        vote = request.POST['choice']
        voteCountry = CountryName.objects.get(code=vote)
        obj = CountryName.objects.all()

        voteCountry.vote = voteCountry.vote + 1
        print(voteCountry.vote)
        voteCountry.save()

        error = ""
        # except Exception as e:
        #     error = "투표할 나라를 선택하세요."
        #     return redirect('vote')
        
        
    context = {'voteCountry': voteCountry, 'obj':obj, 'error':error}
    return render(request, 'country/vote.html', context)

# 국가별로 그래프를 보여주는 뷰
def country(request, code):
    ### 예외처리 적용 시 해당 부분 주석 해제
    try:
        # 국가명을 국가코드에서 가져온다.
        ### 예외처리 적용 시 아래 부분 들여쓰기
        countryName = CountryName.objects.get(code=code)

        yearData = [ i for i in range(2000,2020) ]
        # yearCol = [ 'y' + str(i) for i in range(2000,2020) ] # 사용 안함.
        
        # 빈 리스트에 일치하는 국가명의 DB를 가져온다.
        countryData = list()
        obj = TravelByCountry.objects.get(country=countryName)
        
        # 가져온 data를 딕셔너리로 만든다.
        for key, value in obj.__dict__.items():
            # 해당연도 데이터만 가져와서 변수에 담는다.
            # print(key, value)
            if 'y' == key[0] :
                countryData.append(value)
        
        # data 형식을 변경하여 변수에 담는다.
        commaData = [ format(i, ",") + "명" for i in countryData ]
        
        # data가 없을 경우 메시지를 바꾼다.
        for i, v in enumerate(commaData):
            if v == "0명":
                commaData[i] = "데이터없음"
        
        context = {'code':code, 'countryName':countryName, 'countryData':countryData, 'yearData':yearData, 'commaData':commaData }


    

    ### 예외처리 적용 시 해당 부분 주석 해제
    # 국가명이 없을 경우 국가명 변수에 None을 담는다.
    except Exception as e:
        # print(e)
        countryName = CountryName.objects.get(code=code)
        countryData = None
        yearData = None
        commaData = None
        countryList = CountryName.objects.order_by('c_name')

        context = {'code':code, 'countryName':countryName, 'countryData':countryData, 'yearData':yearData, 'commaData':commaData, 'countryList':countryList }

    return render(request, 'country/country.html', context)



