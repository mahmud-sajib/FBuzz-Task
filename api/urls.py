from django.urls import path

from .import views

urlpatterns = [
    path('', views.info_upload_view, name='home'),
    path('info/', views.info_show, name='info'),
]