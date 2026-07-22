from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_normativ, name='normativ_list'),
    path('create/', views.create_normativ, name='create_normativ'),
    path('<int:pk>/', views.read_normativ, name='read_normativ'),
    path('<int:pk>/update/', views.update_normativ, name='update_normativ'),
    path('<int:pk>/delete/', views.delete_normativ, name='delete_normativ'),

    path('questions/', views.get_normativ_question, name='normativ_question_list'),
    path('questions/create/', views.create_normativ_question, name='create_normativ_question'),
    path('questions/<int:pk>/', views.read_normativ_question, name='read_normativ_question'),
    path('questions/<int:pk>/update/', views.update_normativ_question, name='update_normativ_question'),
    path('questions/<int:pk>/delete/', views.delete_normativ_question, name='delete_normativ_question'),

    path('answers/', views.get_normativ_answer, name='normativ_answer_list'),
    path('answers/create/', views.create_normativ_answer, name='create_normativ_answer'),
    path('answers/<int:pk>/', views.read_normativ_answer, name='read_normativ_answer'),
    path('answers/<int:pk>/update/', views.update_normativ_answer, name='update_normativ_answer'),
    path('answers/<int:pk>/delete/', views.delete_normativ_answer, name='delete_normativ_answer'),
]