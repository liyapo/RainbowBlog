from django.shortcuts import render, redirect
from django.views.generic import UpdateView, CreateView, DeleteView
from .forms import ArticlesForm 
from .models import Articles
import datetime

# Create your views here.
def list_articles(request):
    list_articles = Articles.objects.all()
    context = {'articles': list_articles}
    return render(request, 'articles/listArticles.html', context)

def detail_articles(request, pk):
    detail_articles = Articles.objects.get(pk=pk)
    context = {'articles': detail_articles}
    return render(request, 'articles/detailArticles.html', context)

def create_articles(request):
   
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            articles = form.save(commit=False)
            articles.published_date = datetime.datetime.now()
            articles.save()

            detail_articles = Articles.objects.get(pk=articles.pk)
            context = {'articles': detail_articles}
            return render(request, 'articles/detailArticles.html', context)
    else:
        form = ArticlesForm()
    return render(request, 'articles/createArticles.html', {'form': form})


def edit_articles(request):
    list_articles = Articles.objects.all()
    context = {'articles': list_articles}
    return render(request, 'articles/editArticles.html', context)

    
def edit_this_article(request, pk):
    thisarticle = Articles.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticlesForm(request.POST, instance=thisarticle)
        if form.is_valid():
            thisarticle = form.save(commit=False)
            thisarticle.published_date = datetime.datetime.now()
            thisarticle.save()

            detail_articles = Articles.objects.get(pk=pk)
            context = {'articles': detail_articles}
            return render(request, 'articles/detailArticles.html', context)
    else:
        form = ArticlesForm(instance=thisarticle)
    return render(request, 'articles/editThisArticle.html', {'form': form})


