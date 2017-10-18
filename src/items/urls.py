from django.conf.urls import url
from django.contrib import admin
from items import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.items, name='items'),
    url(r'^add/$', views.add, name = 'add'),
    url(r'^(?P<id>\d+)/$', views.item_detail, name='detail'),
    url(r'^(?P<id>\d+)/buy$', views.buy, name='buy'),
    url(r'^(?P<id>\d+)/remove$', views.remove, name = 'remove'),
    url(r'^update_rating/$', views.update_rating, name = 'update_rating'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)