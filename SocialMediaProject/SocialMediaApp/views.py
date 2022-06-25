from django.shortcuts import render, get_object_or_404,redirect
from .models import Article
from .forms import ArticleCreateForm
import datetime as dt
date1 = dt.datetime.now().date()

# Create your views here.

def ArticleList(request):
    articles = Article.objects.all()
    return render(request, 'articlelist.html',{'articles':articles})
"""
def articleDetail(request,id):
    article = Article.objects.get(id=id)
    return render(request,'article.html',{'article':article})
"""

def Article_detail(request,id,slug):
    article =get_object_or_404(Article,id=id,slug=slug)
    return render(request,'article.html',{'article': article})
def Article_create(request):
    if request.method == 'POST':
        form = ArticleCreateForm(request.POST)
        if form.is_valid():
            title1 = request.POST.get('title'),
            body1 = request.POST.get('body')
            Article(
            title = title1,
            body = body1,
            author = request.user,
            created_date = date1
            ).save()
            return redirect('article_list')

    else:
        form =ArticleCreateForm()
        return render(request,'Article_create.html',{'form':form})
