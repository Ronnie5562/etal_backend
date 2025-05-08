from django.contrib import admin
from django.utils.translation import gettext as _
from .models import Tag, Post, PostLike, PostComment


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'created_at',
    ]
    search_fields = [
        'name',
    ]
    readonly_fields = ['created_at']
    ordering = ('-created_at',)

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'name',
                )
            }
        ),
        (
            _('Timestamps'),
            {
                'fields': (
                    'created_at',
                )
            }
        ),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'text',
        'media',
        'created_at',
        'updated_at',
    ]
    search_fields = [
        'title', 'text',
    ]
    readonly_fields = ['created_at', 'updated_at']
    ordering = ('-created_at',)

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'title',
                    'text',
                    'media',
                    'tags',
                )
            }
        ),
        (
            _('Timestamps'),
            {
                'fields': (
                    'created_at',
                    'updated_at',
                )
            }
        ),
    )


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'post',
        'created_at',
    ]
    search_fields = [
        'user', 'post',
    ]
    readonly_fields = ['created_at']
    ordering = ('-created_at',)

    fieldsets = (
        (
            _('User'),
            {
                'fields': (
                    'user',
                )
            }
        ),
        (
            _('Post'),
            {
                'fields': (
                    'post',
                )
            }
        ),
        (
            _('Timestamps'),
            {
                'fields': (
                    'created_at',
                )
            }
        ),
    )


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'post',
        'text',
        'created_at',
        'updated_at',
    ]
    search_fields = [
        'user', 'post', 'text',
    ]
    readonly_fields = ['created_at', 'updated_at']
    ordering = ('-created_at',)

    fieldsets = (
        (
            _('User'),
            {
                'fields': (
                    'user',
                )
            }
        ),
        (
            _('Post'),
            {
                'fields': (
                    'post',
                )
            }
        ),
        (
            _('Comment'),
            {
                'fields': (
                    'text',
                )
            }
        ),
        (
            _('Timestamps'),
            {
                'fields': (
                    'created_at',
                    'updated_at',
                )
            }
        ),
    )
