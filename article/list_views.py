from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import ArticleColumn,ArticlePost
from django.contrib.auth.models import User

def article_titles(request,username=None):
    if username:
        user=User.objects.get(username=username)
        article_title=ArticlePost.objects.filter(username=username)
    else:
        article_title=ArticlePost.objects.all()
    articles_list=ArticlePost.objects.filter(author=request.user)
    pagintor=Paginator(articles_list,2)
    page=request.GET.get("page")
    try:
        current_page=pagintor.page(page)
        articles=current_page.object_list
    except PageNotAnInteger:
        current_page=pagintor.page(1)
        articles=current_page.object_list
    except EmptyPage:
        current_page=pagintor.page(pagintor.num_pages)
        articles=current_page.object_list
    return render(request,"article/list/article_titles.html",{"articles":articles,"page":current_page})

def article_detail(request,id,slug):
    article=get_object_or_404(ArticlePost,id=id,slug=slug)
    return render(request,"article/list/article_content.html",{"article":article})