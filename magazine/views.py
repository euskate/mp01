from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
#BLOB 읽기용
from base64 import b64encode # byte배열을 base64로 변경함.
import pandas as pd
import time

import pandas as pd
import glob

# Create your views here.
# def index(request):
#     return render(request, "index.html")


# def index(request):
#     return render(request, "magazine/try2.html")

# def main1(request):
#     return render(request, "magazine/trend2020.html")

# def main2(request):
#     return render(request, "magazine/Elsa.html")

# def main3(request):    
#     return render(request, "magazine/trip_trend.html")


    