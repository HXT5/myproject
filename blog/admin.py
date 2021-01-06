from django.contrib import admin
from .models import BlogArticles
# Register your models here.

class BlogArticlesAdmin(admin.ModelAdmin):
    '''设置列表可显示的字段'''
    list_display = ('title', 'auth', 'body', 'publish',)

    '''设置过滤选项'''
    list_filter = ('auth', 'publish',)

    '''每页显示条目数'''
    list_per_page = 5

    '''设置可编辑字段'''
    #list_editable = ('title',)

    '''设置带链接的字段'''
    list_display_links=('title',)

    '''按日期月份筛选'''
    date_hierarchy = 'publish'

    '''按发布日期排序'''
    ordering = ('-publish',)

    '''可以搜素的字段'''
    search_fields = ('title',)

    '''用于单对多关系'''
    raw_id_fields = ('auth',)

admin.site.register(BlogArticles, BlogArticlesAdmin)
