from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Article, Purchase, ArticleForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import qrcode
import requests
import json

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

def home(request):
    articles = Article.objects.values
    context = {'articles': articles}
    return render(request, 'lightning/home.html', context)


@login_required
def article(request, article_id):
    article = Article.objects.get(id=article_id)
    user = request.user
    
    try:
        purchase = Purchase.objects.get(user=user, article=article)
        
        if not purchase.paid:
            payload = {'payment_hash': purchase.payment_hash}
            ln_response = requests.post(f'https://legend.lnbits.com/paywall/api/v1/paywalls/check_invoice/{article.paywall_id}', 
                                        data=json.dumps(payload))
            ln_json = ln_response.json()
            paid = ln_json['paid']
            if paid:
                purchase.paid = paid
                article.revenue += article.price
                purchase.save()
                article.save()
        
    except:
        payload = {'amount': article.price}
        ln_response = requests.post(f'https://legend.lnbits.com/paywall/api/v1/paywalls/invoice/{article.paywall_id}', 
                                    data=json.dumps(payload))
        ln_json = ln_response.json()
        
        purchase = Purchase(
            user=user,
            article=article,
            payment_hash=ln_json['payment_hash'],
            payment_request=ln_json['payment_request'],
            paid=False
        )
        purchase.save()
    
    context = {'article': article, 'user': user, 'purchase': purchase}
    return render(request, 'lightning/article.html', context)


@login_required
def article_form(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = ArticleForm()
    return render(request, "lightning/article_form.html", {'form': form})