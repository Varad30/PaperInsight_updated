from . import views
from django.urls import path, include

urlpatterns = [
    path('upload/', views.upload_files, name='upload'),
    path('uploadimg/', views.upload_files2, name='uploadimg'),


]