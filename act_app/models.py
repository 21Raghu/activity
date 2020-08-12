from django.db import models

class member(models.Model):

    id = models.CharField(primary_key=True,max_length=10)
    real_name=models.CharField(max_length=30)


    timezone = models.CharField(max_length=32,  default='UTC')

class activity(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    start_time= models.TimeField()
    end_time =models.TimeField()