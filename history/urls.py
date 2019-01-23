from django.urls import path

from . import views

app_name = "history"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:artist_id>/', views.detail, name='detail'),
]

