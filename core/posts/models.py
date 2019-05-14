from django.db import models
from django.utils.text import slugify

from core import settings


# Create your models here.

class Book(models.Model):
    isbn = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    cover_image = models.ImageField()

class Post(models.Model):
    poster = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )
    draft_started_datetime = models.DateTimeField(auto_now_add=True, editable=False)
    last_update = models.DateTimeField(auto_now=True, editable=False)
    visible = models.BooleanField(default=True)
    publish_at = models.DateTimeField(auto_now=False)

    post_title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)
    post_contents = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-publish_at']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.post_title,self.pk)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.post_title