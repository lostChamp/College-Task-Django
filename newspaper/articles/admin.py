from django.contrib import admin
from .models import Article, Comment

from . import models

class CommentInLine(admin.TabularInline):
    model = models.Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)


# Register your models here.
