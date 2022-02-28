from django.contrib import admin
from Boomie.models import Category, Post, Comment, ReplyComment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    # exclude = ['images', 'views', 'categories']

class CategoryAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(ReplyComment)
