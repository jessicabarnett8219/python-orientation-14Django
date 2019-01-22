from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artist/', views.artist, name='artist'),
    path('<int:artist_id>/', views.detail, name='detail'),
]