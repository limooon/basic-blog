from django.contrib import admin
from .models import Favorites

class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('user', 'entry',)
    list_filter = ('user', 'entry',)
    search_fields = ('user__username', 'entry__title',)
    readonly_fields = ('created', 'modified',)

admin.site.register(Favorites, FavoritesAdmin)
