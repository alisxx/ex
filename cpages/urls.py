from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
        path('', views.home, name='home'),
        path('index/', views.index, name='index'),
        path('index/contact/', views.contact, name='contact'),
        path('index/careers/', views.careers, name='careers'),
        path('index/service', views.service, name='service'),
        ]

urlpatterns += staticfiles_urlpatterns()
