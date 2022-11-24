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