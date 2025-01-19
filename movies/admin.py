from django.contrib import admin
from .models import Movie, Comment
from django_summernote.admin import SummernoteModelAdmin
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url



@admin.register(Movie)
class MovieAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'movie', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        if queryset is not None:
            queryset.update(approved=True)