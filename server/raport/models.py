from django.db import models

# Create your models here.

class Users(models.Model):
    user_id=models.IntegerField(primary_key=1)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class raport(models.Model):
    report_id=models.IntegerField(primary_key=1)
    user_id=models.IntegerField(models.ForeignKey(Users, to_field='user_id', on_delete=models.CASCADE))
    geocode=models.CharField(max_length=200)
    path_to_Photo=models.CharField(max_length=200)



    
