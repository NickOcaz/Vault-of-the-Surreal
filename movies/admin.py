from django.contrib import admin
from .models import Movie, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Movie)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('Title', 'Slug', 'Status')
    search_fields = ['Title']
    list_filter = ('Status',)
    prepopulated_fields = {'Slug': ('Title',)}
    summernote_fields = ('Content',)


# Register your models here.
# admin.site.register(Movie)
admin.site.register(Comment)
