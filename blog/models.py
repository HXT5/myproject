from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
# manage.py makemigrations创建数据库表文件
# manage.py migrate创建数据库
# 创建管理员 manage.py createsuperuser
class BlogArticles(models.Model):
    title = models.CharField(max_length=500)
    auth = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ("-publish",)#class Meta做为嵌套类，主要目的是给上级类添加一些功能，或者指定一些标准.
    def __str__(self):
        return "hello"
