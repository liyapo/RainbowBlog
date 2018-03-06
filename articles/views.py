from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import UpdateView, CreateView, DeleteView
from .forms import ArticlesForm, ArticlesUserForm, UserSignUpForm, UserLoginForm
from .models import Articles
import datetime
from django.http import HttpResponse

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
        form = ArticlesUserForm(request.POST)
        if form.is_valid():
            articles = form.save(commit=False)
            articles.published_at = datetime.datetime.now()
            articles.author = request.user
            articles.save()

            detail_articles = Articles.objects.get(pk=articles.pk)
            context = {'articles': detail_articles}
            return render(request, 'articles/detailArticles.html', context)
    else:
        form = ArticlesUserForm()
    return render(request, 'articles/createArticles.html', {'form': form})


def edit_articles(request):
    author = False
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

def delete_article(request, pk):
    Articles.objects.filter(id=pk).delete()
    list_articles = Articles.objects.all()
    context = {'articles': list_articles}
    return render(request,'articles/editArticles.html',context)

def sign_up(request):
    # A boolean value to check if the signup is successful
    success = False

    # If it is a HTTP POST, we process form data
    if request.method == "POST":
        # Get the info from the form
        form = UserSignUpForm(request.POST)
        # If form is valid then we save new user
        if form.is_valid():
            new_user = form.save(commit=False)
            # We hash the password and update the user object
            password = new_user.set_password(new_user.password)
            
            #articles.published_date = datetime.datetime.now()
            new_user.save()

            #password = new_user.set_password(new_user.password)
            #username = new_user.get_username()
            success = True

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)
            
            return render(request, 'articles/signUp.html', {'success': success})
    else:
        form = UserSignUpForm()
    return render(request, 'articles/signUp.html', {'form': form, 'success': success})


def login_user(request):

    form = UserLoginForm()
    exsist = True
    # If the request is a HTTP POST, get the info
    if request.method == 'POST': 
        # Gather the username, password
        username = request.POST['username']
        password = request.POST['password']
        # Django authentication, is combination is valid the user object is returned 
        user = authenticate(username=username, password=password)
        # If we have user object, we log him in
        # If none then we return the mistake
        if user:  
            exsist = True
            login(request, user)
            return render(request, 'rainbow/home.html')  
        else: 
            exsist = False
            return render(request, 'articles/login.html', {'form': form, 'exsist':exsist})
    # The request is not HTTP POST
    else:
        return render(request, 'articles/login.html', {'form': form, 'exsist':exsist})


def logout_user(request):
    logout(request)
    return render(request, 'rainbow/home.html')

 
