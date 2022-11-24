from django.contrib import admin

from .models import Article, Purchase

admin.site.register(Article)
admin.site.register(Purchase)