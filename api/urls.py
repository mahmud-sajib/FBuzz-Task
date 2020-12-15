from django.urls import path

from .import views

urlpatterns = [
    path('', views.info_upload_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('info/', views.info_show, name='info'),
    path('cv-upload/', views.cv_file_upload, name='cv-upload'),
    path('cv-upload-success/', views.cv_upload_success, name='cv-upload-success'),
]