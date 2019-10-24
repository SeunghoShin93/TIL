from django.contrib import admin
from .models import Article, Comment
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at')

admin.site.register(Comment, CommentAdmin)