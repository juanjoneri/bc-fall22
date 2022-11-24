from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Article
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'lightning/signup.html', {'form': form})

def index(request):
    articles = Article.objects.values
    context = {'articles': articles}
    return render(request, 'lightning/index.html', context)

@login_required
def article(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {'article': article, 'user': request.user}
    return render(request, 'lightning/article.html', context)