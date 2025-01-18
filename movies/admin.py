from django.contrib import admin
from .models import Movie, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Movie)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('Content',)


admin.site.register(Comment)
