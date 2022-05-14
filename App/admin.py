from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from App.models import Category, Post, Comment, ReplyComment

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(ReplyComment)
