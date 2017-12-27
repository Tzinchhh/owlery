from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('alltables.urls', namespace='account')),
    url(r'^', include('django.contrib.auth.urls')),
    (r'^messages/', include('django_messages.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns  += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)