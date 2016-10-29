from django.contrib import admin
from .models import Post,Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'cover', 'user', 'category')
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
