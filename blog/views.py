from django.shortcuts import render,get_object_or_404
from .models import BlogArticles

# Create your views here.
def blog_title(request):
    blogs = BlogArticles.objects.all()
    '''render（）的 作用是将数据渲染到指定模板上'''
    return render(request, "blog/titles.html", {"blogs": blogs})


def blog_article(request, article_id):
    #articles = BlogArticles.objects.get(id=article_id)
    articles = get_object_or_404(BlogArticles,id=article_id)
    return render(request, "blog/content.html", {"articles": articles})