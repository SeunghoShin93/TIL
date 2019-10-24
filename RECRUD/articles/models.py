from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'글제목 : {self.title} 글내용 : {self.content}' 

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'댓글 내용: {self.content} 작성 시간: {self.created_at}'