from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    price = models.IntegerField()
    revenue = models.IntegerField()
    paywall_id = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.title}'