from django.contrib import admin
from blog.models import BlogPost


@admin.register(BlogPost)
class BlodPostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "content",
        "is_published",
        "views",
        "created_at",
    )
    list_filter = (
        "title",
        "views",
        "is_published",
        "created_at",
    )
    search_fields = (
        "name",
        "title",
    )
