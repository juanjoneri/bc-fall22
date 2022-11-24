from django.db import models
from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    price = models.IntegerField()
    revenue = models.IntegerField()
    paywall_id = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.title}'
    
class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    payment_hash = models.TextField()
    payment_request = models.TextField()
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.username} ({self.article.title})'