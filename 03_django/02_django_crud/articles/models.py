from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail
from django.urls import reverse
from django.db import models


def articles_image_path(instance, filename):
    return f'articles/{instance.pk}/images/{filename}'


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    # image_thumbnail = ImageSpecField(
    #     source='image',  # 원본 ImageField 이름
    #     processors=[Thumbnail(200, 300)],
    #     format='JPEG',
    #     options={'quality': 90},
    # )

    image = ProcessedImageField(
        # ProcessedImageField 에 인자로 들어가 있는 값들은 migrations 이후에
        # 추가되거나 수정되더라도 makemigrations 를 하지 않아도 된다.
        processors=[Thumbnail(200, 300)],
        format='JPEG',  # 저장 포맷 , jpeg: 원본 퀄리티 유지에 좋음
        options={'quality': 90},  # 추가 옵션들
        upload_to='articles/images',  # 저장 위치 (MEDIA_ROOT/articles/images)
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return self.title
        return f'<Article({self.article_id}): Comment({self.article_pk})-{self.content}'

    def get_absolute_url(self):
        # return f'/articles/{self.pk}/'
        # articles/10/
        return reverse('articles:detail', kwargs={'article_pk': self.pk})
        # return reverse('articles:detail', kwargs={'pk': self.pk}) # articles/10/
        # 주의 사항
        # reverse 함수에 args 와 kwargs를 동시에 인자로 보낼 수 없다.


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE,)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.content
