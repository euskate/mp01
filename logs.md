## 2019. 1. 20.
- Magazine 템플릿 생성 중
- MongoDB 데이터 전처리
- 국가별 코드 위키 크롤링
- 국가별 코드 oracleDB 연동

## 2019. 1. 17.
- 박소현 : 여행 관련 data 수집 및 정리
- 서연주 : PPT template 검색 및 결정
- 장원 : jvectormap 라이브러리에 링크 가능하게 연결
- 정석원 : 대륙별 data 몽고DB에 입력

## 2019. 1. 16.
- 월별 통계 중 한국 출입국 부분을 잘라서 몽고DB에 넣기 시도.
- 딕셔너리화 하여 몽고DB에 넣기 성공! (정석원)
- 정석원의 Idea를 조원들과 함께 공유.
- 웹의 첫페이지 만드는 중 (장원)
    - 기본세팅, 부트스트랩, 지도

## 2019. 1. 15
- 출입국 관광 통계 자료 수집(메인 자료 / 한국관광공사) (서연주)
- [1984-2018년 출입국 국가별 월별통계](https://kto.visitkorea.or.kr/kor/notice/data/statis/profit/board/view.kto?id=423699&isNotice=true&instanceId=294&rnum=0)

## 2019. 1. 14.
- 인천국제항공사 자료 수집 (박소현)


# 장고 홈페이지 제작 log 중
- 프로젝트 생성 : 프로젝트명은 임시로 mp01(첫번째 미니프로젝트)로 정함
    - django-admin startproject mp01

- setting.py 설정
1. 템플릿 설정
```
TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
```
1. 스태틱 경로 설정

    `STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]`

1. Database 설정

DATABASES = {
    'default': {
        # oracle
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'xe', #SID
        'USER': 'admin',
        'PASSWORD' : '1234',
        'HOST' : '192.168.99.100',
        'PORT' : '32764'
    }
}

1. Time Zone 설정

    TIME_ZONE = 'Asia/Seoul'

- 상위폴더에 홈페이지 설정
    - urls.py 추가
```
from mp01 import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
```

    - views.py 생성


- 장고 버전을 2.2.5로 다운그레이드 해야 한다. (모델관련 에러발생)
    - conda list django
    - conda install django==2.2.5


## 첫 페이지에 지도 가져오기
- jvectormap 라이브러리
    - http://jvectormap.com/
    - 아직 실력이 부족하여 어떻게 적용하여야할지 모르겠다!
    - 인터넷 검색해서 나온 html 코드를 가져옴! https://codepen.io/michaelgermini/pen/QyjrZb

### 첫 페이지 국가 클릭하면 국가별 페이지로 연결
- jvectormap 라이브러리 수정


## 멤버 앱 만들기
- 기존 수업 auth부분을 사용