from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url 

urlpatterns = [
    url('media/<path>', serve, {document_root: settings.MEDIA_ROOT}),
    
    path('admin/', admin.site.urls),
    path('boomie/', include('Boomie.urls')),
    path('', include('users.urls')),
    path('summernote/', include('django_summernote.urls')),
]

urlpatterns += staticfiles_urlpatterns()#This serves static files