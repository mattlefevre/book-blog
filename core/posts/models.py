from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify

from core import settings


# Create your models here.


class Book(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    synopsis = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(blank=True, null=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)

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
    post_contents = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ["-publish_at"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.post_title, self.pk)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.post_title
