1. github 다운받은 폴더를 프로젝터 폴더에 푼다
    - 도커와 oracle12c, mongodb 실행한다.
        1. docker start oracle12c
        1. docker start mongodb
2. 장고 모델 마이그레이션
    - (콘솔 프롬프트 / 프로젝트 폴더에서)
    - python manage.py check
    - python manage.py migrate
3. 데이터베이스 크롤링 및 가져오기
    - (VS CODE로 작업 폴더를 연다)
    - 국가별 코드 가져오기
        1. resource/code_crawl.py 실행 => 크롤링해서 몽고db에 저장
        2. resource/code_MtoO.py 실행     => 오라클 테이블에 저장
    - 국가별 데이터 가져오기(연도별)
        1. resource/year_mongo.py 실행 => total_year.csv를 몽고db에 저장
        2. resource/year_MtoO.py 실행 => 오라클 테이블로 저장
    - 대륙 데이터 가져오기
        1. resource/cont_oracle.py 실행
    