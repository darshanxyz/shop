from django.conf.urls import url
from django.contrib import admin
from user_account import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^login/', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register$', views.RegistrationFormView.as_view(), name='reg_home'),
    url(r'^$', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)