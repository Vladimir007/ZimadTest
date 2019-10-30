from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.static import serve

from ZimadTest import views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', views.IndexView.as_view(), name='index'),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('media/<path>', serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
]

if settings.DEBUG:
    # Just for development purposes
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
