from django.db import models

# Create your models here.
class Entry(models.Model):
    # id = models.IntegerField(auto_created=True, unique=True)
    title = models.CharField(max_length=200, null=True)
    content = models.CharField(max_length=5000)
    category = models.CharField(max_length=50, null=True)
    # category = models.C
    entry_date = models.DateTimeField(auto_now=True)
    user_name = models.CharField(max_length=200)

# TODO ex.workユーザー管理するワーク
class User(models.Model):
    user_name = models.CharField(max_length=200,unique=True,primary_key=True)
    authorname = models.CharField(max_length=200, default="")
    mail = models.EmailField(unique=True)
