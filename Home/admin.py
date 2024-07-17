from django.contrib import admin
from .models import Home, Suscriber, Contact

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Suscriber)
class SuscriberAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email',)
    search_fields = ('full_name', 'email',)
