from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    group = models.ForeignKey('Group', on_delete=models.CASCADE, blank=True, null=True)

    
class Group(models.Model):
    group_id = models.CharField(primary_key=True, max_length=1000)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=80, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    