from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Article(models.Model):
    # 作家
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='articles')
    # タイトル
    title = models.CharField(max_length=100)
    # 本文
    body = models.TextField()
    # 作成時間
    created = models.DateTimeField(default=timezone.now)
    # 更新時間
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
