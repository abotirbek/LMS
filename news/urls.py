from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_news, name='news_list'),
    path('create/', views.create_news, name='create_news'),
    path('<int:pk>/', views.read_news, name='read_news'),
    path('<int:pk>/update/', views.update_news, name='update_news'),
    path('<int:pk>/delete/', views.delete_news, name='delete_news'),
]