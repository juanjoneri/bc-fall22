from django.db import models
from django.conf import settings
from django.forms import ModelForm


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    price = models.IntegerField()
    revenue = models.IntegerField(default=0)
    paywall_id = models.CharField(max_length=200, default='2AA6BgQGksioyzvwBTdwLP')
    
    def __str__(self):
        return f'{self.title}'
    
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'price']
    
class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    payment_hash = models.TextField()
    payment_request = models.TextField()
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.username} ({self.article.title})'