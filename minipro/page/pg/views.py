from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
#BLOB 읽기용
from base64 import b64encode 
import pandas as pd
import time

import pandas as pd
import glob


# Create your views here.
# def index(request):
#     return render(request, "index.html")


def index(request):
    return render(request, "try2.html")

def main1(request):
    return render(request, "trend2020.html")

def main4(request):
    return render(request, "feb.html")



    