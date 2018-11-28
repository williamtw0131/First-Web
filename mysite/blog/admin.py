from django.contrib import admin


# 2018/11/21
from .models import Post, Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
