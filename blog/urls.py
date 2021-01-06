from django.conf.urls import url
from . import views
app_name = 'blog'
urlpatterns=[
    url(r'^$', views.blog_title, name="blog_title"),
    #该数字字符赋给article_id 参数
    url(r'(?P<article_id>\d)/$', views.blog_article, name="blog_detail"),
]