from django.shortcuts import render
from .models import Articles

# Create your views here.
def list_articles(request):
    list_articles = Articles.objects.all()
    context = {'articles': list_articles}
    return render(request, 'articles/listArticles.html', context)

def detail_articles(request, pk):
    article = Articles.objects.get(pk=pk)
    context = {'detail_articles': detail_articles}
    return render(request, 'articles/detailArticles.html', context)

def create_articles(request):
    return render(request, 'articles/createArticles.html')

def edit_articles(request):
    return render(request, 'articles/editArticles.html')


