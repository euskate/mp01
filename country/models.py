from django.db import models

# Create your models here.

class CountryName(models.Model):
    code    = models.CharField(primary_key=True, max_length=2)
    c_name  = models.CharField(max_length=30)

    def __str__(self):
        return self.c_name

class TravelByCountry(models.Model):
    id          = models.AutoField(primary_key=True) # 자동생성
    continent   = models.CharField(max_length=10) # 대륙
    country     = models.CharField(max_length=30) # 나라
    y2000       = models.IntegerField() # 연도별 출국자 2000~2018년
    y2001       = models.IntegerField()
    y2002       = models.IntegerField()
    y2003       = models.IntegerField()
    y2004       = models.IntegerField()
    y2005       = models.IntegerField()
    y2006       = models.IntegerField()
    y2007       = models.IntegerField()
    y2008       = models.IntegerField()
    y2009       = models.IntegerField()
    y2010       = models.IntegerField()
    y2011       = models.IntegerField()
    y2012       = models.IntegerField()
    y2013       = models.IntegerField()
    y2014       = models.IntegerField()
    y2015       = models.IntegerField()
    y2016       = models.IntegerField()
    y2017       = models.IntegerField()
    y2018       = models.IntegerField()
    y2019       = models.IntegerField()

    def __str__(self):
        return self.country
