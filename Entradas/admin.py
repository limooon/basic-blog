from django.contrib import admin
from .models import Category, Tag, Entry

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name')
    search_fields = ('name', 'short_name')
    list_filter = ('name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'public', 'portada', 'in_home')
    list_filter = ('user', 'category', 'public', 'portada', 'in_home')
    search_fields = ('title', 'resume', 'content')
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Entry, EntryAdmin)
