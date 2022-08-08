from django.contrib import admin
from .models import Topic, Thread, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Topic)
class TopicAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', 'created_on', 'approved')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    summernote_fields = ('content')
    actions = ['approve_threads']

    def approve_threads(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
