from django.urls import path

from .import views

urlpatterns = [
    path('', views.login_view, name='home'),
    path('info-upload/', views.info_upload_view, name='info-upload'),
    path('cv-upload/', views.cv_file_upload_view, name='cv-upload'),
]