from django.contrib import admin
from Post.models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"urlName": ("name",)}

admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)

