from django.urls import path
from . import views

urlpatterns = [
    path('home', views.kanji_list, name='kanji_list'),
    path('', views.kanji_list, name='kanji_list'),
    path('kanji/<int:pk>/', views.kanji_detail, name='kanji_detail'),
    path('kanji/new/', views.kanji_create, name='kanji_create'),
    path('kanji/<int:pk>/edit/', views.kanji_update, name='kanji_update'),
    path('kanji/<int:pk>/delete/', views.kanji_delete, name='kanji_delete'),
]