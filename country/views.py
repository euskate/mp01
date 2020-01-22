from django.shortcuts import render, get_object_or_404
from .models import CountryName, ContinentName, TravelByCountry
# Create your views here.

# 순위를 보여주는 뷰
def top(request):
    # 연도별로 위에서부터 3개만 가져 옴
    obj = TravelByCountry.objects.all().order_by('-y2010')[1:4]

    test_coun = list()
    test_data = list()
    
    # 콘솔에서 확인
    for i in obj:
        test_coun.append(i.country)
        test_data.append(i.y2010)
    
    print(test_coun)
    print(test_data)

    # test_coun 변수 : top 3 국가명 (막대 그래프 y축의 라벨명)
    # test_data 변수 : 여행객 수 (막대 그래프의 길이)

    # 여기 아래에다가 차트 구현을 해서 템플릿으로 넘겨 봅시다. (템플릿은 /template/top.html에 있음.)




    # 화이팅!

    return render(request, 'country/top.html')


# 대륙별로 그래프를 보여주는 뷰
def continent(request, cont):
    contName = get_object_or_404(ContinentName, cont=cont)

    obj = TravelByCountry.objects.filter(continent__contains=str(contName))

    print(obj)

    for i in obj:
        print(i)

    # countryName = CountryName.objects.get(code=code)

    # yearData = [ i for i in range(2000,2020) ]
    # # yearCol = [ 'y' + str(i) for i in range(2000,2020) ] # 사용 안함.
    
    # # 빈 리스트에 일치하는 국가명의 DB를 가져온다.
    # countryData = list()
    # obj = TravelByCountry.objects.get(country=countryName)
    
    # # 가져온 data를 딕셔너리로 만든다.
    # for key, value in obj.__dict__.items():
    #     # 해당연도 데이터만 가져와서 변수에 담는다.
    #     if 'y' == key[0] :
    #         countryData.append(value)
    
    # # data 형식을 변경하여 변수에 담는다.
    # commaData = [ format(i, ",") + "명" for i in countryData ]
    
    # # data가 없을 경우 메시지를 바꾼다.
    # for i, v in enumerate(commaData):
    #     if v == "0명":
    #         commaData[i] = "데이터없음"






    context = {'cont':contName, 'obj':obj }

    return render(request, 'country/continent.html', context )



# 국가별로 그래프를 보여주는 뷰
def country(request, code):
    ### 예외처리 적용 시 해당 부분 주석 해제
    #try:
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
        if 'y' == key[0] :
            countryData.append(value)
    
    # data 형식을 변경하여 변수에 담는다.
    commaData = [ format(i, ",") + "명" for i in countryData ]
    
    # data가 없을 경우 메시지를 바꾼다.
    for i, v in enumerate(commaData):
        if v == "0명":
            commaData[i] = "데이터없음"

    

    ### 예외처리 적용 시 해당 부분 주석 해제
    # 국가명이 없을 경우 국가명 변수에 None을 담는다.
    # except Exception as e:
    #     print(e)
    #     countryName = None
    #     countryData = None
    #     yearData = None
    
    context = {'countryName':countryName, 'countryData':countryData, 'yearData':yearData, 'commaData':commaData}

    return render(request, 'country/country.html', context)



