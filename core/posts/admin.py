from django.contrib import admin
from core.posts.models import Post, Book

# Register your models here.
admin.site.register(Post)
admin.site.register(Book)
