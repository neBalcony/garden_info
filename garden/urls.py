from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('card/<int:id>/', views.card_detail, name='card_detail'),
    path('', views.tags_list, name='tags_list'),
]
