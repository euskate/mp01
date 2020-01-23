import numpy as np
import pandas as pd
import seaborn as sns
from base64 import b64encode 
import cx_Oracle as oci
import matplotlib.pyplot as plt
import csv

from django.db.models import Sum, Max, Min, Count, Avg
import pandas as pd #conda install pandas
import matplotlib.pyplot as plt
import io # byte로 변환
import base64 # byte를 base64로 변경
from matplotlib import font_manager, rc #한글 폰트 적용

# 일본 중국 베트남그래프
plt.plot([1064390,1133971,1271835,1459333,1588472,1747171,2117325,2600694,2382397,1586772,2439816,1658073,2042775,2456165,2755313,4002095,5090302,7140438,7538952,5337615])
plt.plot ([1344721,1678836,2124310,1945500,2844893,3545341,3923986,4776752,3960392,3197500,4076400,4185400,4069900,3968998,4181700,4444389,4762163,3854869])
plt.plot ([0,0,0,0,232995,317213,421741,475535,449237,362115,495902,536408,700917,748727,832969,1152349,1543883,2415245,3435406,3866066])
plt.show()
