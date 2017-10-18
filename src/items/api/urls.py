from django.conf.urls import url
from django.contrib import admin
from items.api import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.ItemListAPIView.as_view(), name='items'),
    # url(r'^add/$', views.add, name = 'add'),
    url(r'^(?P<pk>\d+)/$', views.ItemRetrieveAPIView.as_view(), name='item-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)