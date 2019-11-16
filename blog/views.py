from django.shortcuts import render,HttpResponse
from .models import BlogArticles
# Create your views here.
def blog_title(request):
    blogs=BlogArticles.objects.all()
    return render(request,'blog/titles.html',{"blogs": blogs})
def blog_article(request,article_id):
    article=BlogArticles.objects.get(id=article_id)
    pub=article.publish
    return render(request,'blog/content.html',{"pblish":pub,"article":article})