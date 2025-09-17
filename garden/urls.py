from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [


    path('card/<int:id>/', views.card_detail, name='card_detail'),

    # админские страницы для работы с метками и карточками
    path('admin/tags/', views.tags_list, name='tags_list'),
    path('admin/tags/create/', views.tag_create, name='tag_create'),
    path('admin/cards/create/', views.card_create, name='card_create'),
]
