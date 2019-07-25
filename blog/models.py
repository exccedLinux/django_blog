# blog/models.py
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
            'auth.User',
            on_delete = models.CASCADE
    )
    body = models.TextField()

    def __str__(self):  #  글 제목이 목록에 보이게 함
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
