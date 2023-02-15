from django.contrib import admin
from .models import IndexInfo, BlogPost, Comment, Blogger


class IndexInfoAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date", "body")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("blog_post", "user", "comment")


class BloggerAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "description")


admin.site.register(IndexInfo, IndexInfoAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Blogger, BloggerAdmin)
