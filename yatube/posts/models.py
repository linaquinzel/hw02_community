from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField()

    pub_date = models.DateTimeField(verbose_name="date published",
                                    auto_now_add=True)
    author = models.ForeignKey(User, verbose_name="author",
                               on_delete=models.CASCADE)
    group = models.ForeignKey("Group", on_delete=models.SET_NULL,
                              blank=True, null=True, to_field='id',
                              related_name="posts_unique")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-pub_date']


class Group(models.Model):
    title = models.CharField(verbose_name="title", max_length=200)
    slug = models.SlugField(unique=True, verbose_name="slug")
    description = models.TextField(verbose_name="description")

    class Meta:
        verbose_name = "Сообщество"
        verbose_name_plural = "Сообщества"

    def __str__(self):
        return self.title
