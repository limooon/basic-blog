
from django.contrib import admin
from django.urls import path, re_path, include 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #re_path('', include('Users.urls')),
    re_path('', include('Users.urls')),
    re_path('', include('Home.urls')),
    re_path('', include('Entradas.urls')),
    re_path('', include('Favoritos.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)