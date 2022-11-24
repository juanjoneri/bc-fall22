from django.http import HttpResponse
from django.template import loader

from .models import Article

def index(request):
    articles = Article.objects.values
    template = loader.get_template('lightning/index.html')
    context = {
        'articles': articles,
    }
    return HttpResponse(template.render(context, request))

def article(request, article_id):
    article = Article.objects.get(id=article_id)
    template = loader.get_template('lightning/article.html')
    context = {
        'article': article,
    }
    return HttpResponse(template.render(context, request))