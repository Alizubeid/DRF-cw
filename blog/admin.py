from django.contrib import admin
from blog.models import Post,Category,Comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
# admin.site.register(Reply)
