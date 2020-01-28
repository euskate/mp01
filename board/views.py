from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from base64 import b64encode    # byte 배열을 base64로 변경함
import pandas as pd

from django.contrib.auth.models import User

# Create your views here.

cursor = connection.cursor()    #sql문 수행을 위한 cursor 객체


@csrf_exempt
def edit(request):
    if request.method == 'GET':
        no = request.GET.get('no', 0)    # no가 없을 경우 default값으로 0을 지정
        sql = """
            SELECT NO, TITLE, CONTENT
            FROM BOARD_BOARD1
            WHERE NO=%s
        """
        cursor.execute(sql, [no])
        data = cursor.fetchone()
        return render (request, 'board/edit.html', {"one":data})
    elif request.method == 'POST':
        no = request.POST['no']
        ti = request.POST['title']
        co = request.POST['content']

        arr = [ti, co, no]

        sql = """
            UPDATE BOARD_BOARD1 SET TITLE=%s,
            CONTENT=%s WHERE NO=%s
        """

        cursor.execute(sql, arr)
        return redirect("/board/content?no="+no)


@csrf_exempt
def delete(request):
    if request.method == 'GET':
        no = request.GET.get('no', 0)    #프로그램이 꺼지지 않게하는 함수
        sql = """
            DELETE FROM BOARD_BOARD1
            WHERE NO=%s
        """
        cursor.execute(sql, [no])
        return redirect("/board")

@csrf_exempt
def content(request):
    if request.method == 'GET':
        no = request.GET.get('no', 0)    #프로그램이 꺼지지 않게하는 함수
        # no = request.GET['no']    #프로그램이 꺼지지 않게하는 함수
        if no == 0:
            return redirect("/board")
        
        if request.session['hit'] == 1:
            # 조회수 1증가시킴
            sql = """
                UPDATE BOARD_BOARD1 SET HIT=HIT+1
                WHERE NO = %s
            """
            cursor.execute(sql, [no])
            request.session['hit'] = 0
        
        sql = """
            SELECT NVL(MAX(NO), 0)
            FROM BOARD_BOARD1
            WHERE NO < %s
        """
        cursor.execute(sql, [no])
        prev = cursor.fetchone()

        sql = """
            SELECT NVL(MIN(NO), 0)
            FROM BOARD_BOARD1
            WHERE NO > %s
        """
        cursor.execute(sql, [no])
        next = cursor.fetchone()



        # 가져오기
        sql = """
            SELECT
                NO, TITLE, CONTENT, WRITER, HIT, TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI:SS'), BOARD_IMG
            FROM
                BOARD_BOARD1
            WHERE
                NO = %s
        """
        cursor.execute(sql, [no])
        data = cursor.fetchone()
        # print(data)

        if data[6]:
            img = data[6].read()        #바이트 배열을 img에 넣음
            img64 = b64encode(img).decode("utf-8")
        else:
            file = open('./static/img/default_image.jpg', 'rb')
            img = file.read()
            img64 = b64encode(img).decode("utf-8")

        # print(no)
        return render (request, 'board/content.html', {"one":data, "image":img64, "prev":prev[0], "next":next[0]})

@csrf_exempt
def list(request):
    if request.method == 'GET':
        request.session['hit'] = 1 # 세션에 hit=1
        
        txt     = request.GET.get("txt","")
        menu    = request.GET.get("menu","")
        page    = int(request.GET.get("page",1))
        ar      = [page*10-9, page*10]
        
        # print(ar)


        # 페이지네이션 하기 전의 코드
        # 
        # sql = """
        #     SELECT
        #         NO, TITLE, WRITER, HIT, TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI:SS')
        #     FROM
        #         BOARD_BOARD1
        #     ORDER BY NO DESC
        # """
        # cursor.execute(sql)
        # data = cursor.fetchall()

        if not txt:     # 검색어가 없는 경우
            sql = """
                SELECT * FROM (
                    SELECT 
                        NO, TITLE, WRITER, HIT, TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI:SS'),
                        ROW_NUMBER() OVER (ORDER BY NO DESC) ROWN
                    FROM
                        BOARD_BOARD1
                        )
                WHERE ROWN BETWEEN %s AND %s
            """
            cursor.execute(sql, ar)
            data = cursor.fetchall()

            # # django Model 사용
            # cnt = Table1.objects.all().count()
            # tot = (cnt-1)//10+2

            # SQL문 사용
            sql = "SELECT COUNT(*) FROM BOARD_BOARD1"
            cursor.execute(sql)
            cnt = cursor.fetchone()[0]
            tot = (cnt-1)//10+2

            # print( type(data) )
            # print( data )           #[(   ), (   )]
        else:       # 검색어가 있는 경우
            ar = ['%'+txt+'%', page*10-9, page*10]
            sql = """
                SELECT * FROM (
                    SELECT 
                        NO, TITLE, WRITER, HIT, TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI:SS'),
                        ROW_NUMBER() OVER (ORDER BY NO DESC) ROWN
                    FROM
                        BOARD_BOARD1
                    WHERE
                        TITLE LIKE %s
                        )
                WHERE ROWN BETWEEN %s AND %s
            """
            cursor.execute(sql, ar)
            data = cursor.fetchall()

            # SQL문 사용
            sql = """
                SELECT
                    COUNT(*)
                FROM 
                    BOARD_BOARD1
                WHERE
                    TITLE LIKE %s
            """
            # ar = ['%'+txt+'%']
            # print(ar)
            # cursor.execute 두번째 항목은 하나라도 리스트에 담아줘야 에러가 안남.
            cursor.execute(sql, [ar[0]])
            cnt = cursor.fetchone()[0]
            # print(cnt)
            tot = (cnt-1)//10+2
            # print(tot)

        return render (request, 'board/list.html', {"list":data, "pages":range(1, tot, 1)})

@csrf_exempt
def write(request):
    if request.method == 'GET':
        # if not request.user.is_authenticated:
        #     return redirect 'member/auth_login')    
        return render (request, 'board/write.html')
    elif request.method == 'POST':
        tmp = None
        if 'img' in request.FILES:
            img = request.FILES['img']  #name값 img
            tmp = img.read()

        arr = [
            request.POST['title'],
            request.POST['contents'],            
            request.user.username,
            tmp
        ]

        try:
            # print(arr)
            sql = """
                INSERT INTO BOARD_BOARD1(TITLE, CONTENT, WRITER, HIT, REGDATE, BOARD_IMG)
                VALUES(%s, %s, %s, 1, SYSDATE, %s)
            """
            cursor.execute(sql, arr)
        except Exception as e:
            print(e)

        return redirect("/board")
    