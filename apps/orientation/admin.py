from django.contrib import admin
from apps.orientation.models import Category, Tag, Orient

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug')
    list_display_links = ('id','title',)
    prepopulated_fields = {"slug": ["title"]}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug')
    list_display_links = ('id','title',)
    prepopulated_fields = {"slug": ["title"]}

@admin.register(Orient)
class OrientAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title',)
    prepopulated_fields = {"slug": ["title"]}