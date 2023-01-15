from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    CATEGORY_CHOICES = (
        ('Training', 'Training'),
        ('Nutrition', 'Nutrition'),
        ('Other', 'Other'),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + "..."


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey('Article', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username
