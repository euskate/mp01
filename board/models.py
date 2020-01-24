from django.db import models

# Create your models here.

class Table1(models.Model):
    objects  = models.Manager() #vs code 오류 제거용

    no      = models.AutoField(primary_key=True)
    title   = models.CharField(max_length=128)
    content = models.TextField() 
    writer  = models.CharField(max_length=32)
    hit     = models.IntegerField()
    b_img   = models.BinaryField(null=True)
    regdate = models.DateTimeField(auto_now_add=True)