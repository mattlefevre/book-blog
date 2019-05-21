from django.db import models
from django.utils.text import slugify

from core import settings


# Create your models here.


class Book(models.Model):
    isbn = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    cover_image = models.ImageField()
    rating = models.PositiveSmallIntegerField(default=1, blank=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    # Automatically-created
    poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    draft_started_datetime = models.DateTimeField(auto_now_add=True, editable=False)
    last_update = models.DateTimeField(auto_now=True, editable=False)
    publish_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=150, default="")
    visible = models.BooleanField(default=True)

    # User-created
    post_title = models.CharField(max_length=100)
    synopsis = models.TextField(null=True, blank=True)
    post_contents = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True)

    class Meta:
        ordering = ["-publish_at"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.post_title, self.pk)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.post_title
