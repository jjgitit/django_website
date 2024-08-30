from django.contrib import admin

#this is where I create models like 'posts' on admin page

from .models import Post

admin.site.register(Post)
