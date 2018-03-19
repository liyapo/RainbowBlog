from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
#from django.views.generic import UpdateView, CreateView, DeleteView
from .forms import ArticlesForm, ArticlesUserForm, UserSignUpForm, UserLoginForm
from .models import Articles
import datetime

# render list of articles
def list_articles(request):
    list_articles = Articles.objects.all()
    context = {'articles': list_articles}
    return render(request, 'articles/listArticles.html', context)

# render specific article
def detail_articles(request, pk):
    detail_articles = Articles.objects.get(pk=pk)
    context = {'articles': detail_articles}
    return render(request, 'articles/detailArticles.html', context)

# create an article, login is required
@login_required(redirect_field_name='login_this_user')
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

# edit/delete articles, login is required, list of all articles is presented
@login_required(redirect_field_name='login_this_user')
def edit_articles(request):
    list_articles = Articles.objects.all()
    context = {'articles': list_articles}
    return render(request, 'articles/editArticles.html', context)

# edit a specific article
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

# delete a specific article
def delete_article(request, pk):
    Articles.objects.filter(id=pk).delete()
    list_articles = Articles.objects.all()
    context = {'articles': list_articles}
    return render(request,'articles/editArticles.html',context)

# Sign up a new user
def sign_up(request):
    # A boolean value to check if the signup is successful
    # html template changes depending on success
    success = False
    # If it is a HTTP POST, we process form data
    if request.method == "POST":
        # Get the info from the form
        form = UserSignUpForm(request.POST)
        # If form is valid then we save new user
        if form.is_valid():
            new_user = form.save(commit=False)
            # update the user object
            password = new_user.set_password(new_user.password)

            new_user.save()
            success = True

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)
            
            return render(request, 'articles/signUp.html', {'success': success})
    else:
        form = UserSignUpForm()
    return render(request, 'articles/signUp.html', {'form': form, 'success': success})

# login an exsisting user
def login_user(request):

    form = UserLoginForm()
    # exsist checks if the user exsists 
    # html template changes depending on exsist 
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

# logout user and send him to home page
def logout_user(request):
    logout(request)
    return render(request, 'rainbow/home.html')

 
