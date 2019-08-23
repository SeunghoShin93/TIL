from django.contrib import admin
from .models import Article  # 명시적 상대경로 표현
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    # 튜플이나 리스트로 작성
    list_display = ('pk', 'title', )
    list_filter = ('created_at',)
    list_display_links = ('content',)
    list_editable = ('title',)
    list_per_page = 2  # 기본값 100


admin.site.register(Article, ArticleAdmin)
