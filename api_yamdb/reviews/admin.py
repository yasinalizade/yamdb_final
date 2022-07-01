from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'description', 'category')
    search_fields = ('name',)
    list_filter = ('year', 'genre', 'category')


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'text', 'author', 'score', 'pub_date'
    )
    search_fields = ('text',)
    list_filter = ('title', 'score')


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'review', 'text', 'author', 'pub_date'
    )
    search_fields = ('text',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
