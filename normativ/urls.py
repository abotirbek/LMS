from django.urls import path
from normativ.normativ_views import normativ_answer_views, normativ_question_views

urlpatterns = [
    path('questions/', normativ_question_views.get_normativ_question, name='normativ_question_list'),
    path('questions/create/<int:pk>/', normativ_question_views.create_normativ_question, name='create_normativ_question'),
    path('questions/<int:pk>/', normativ_question_views.read_normativ_question, name='read_normativ_question'),
    path('questions/<int:pk>/update/', normativ_question_views.update_normativ_question, name='update_normativ_question'),
    path('questions/<int:pk>/delete/', normativ_question_views.delete_normativ_question, name='delete_normativ_question'),

    path('answers/', normativ_answer_views.get_normativ_answer, name='normativ_answer_list'),
    path('answers/create/<int:pk>/', normativ_answer_views.create_normativ_answer, name='create_normativ_answer'),
    path('answers/<int:pk>/', normativ_answer_views.read_normativ_answer, name='read_normativ_answer'),
    path('answers/<int:pk>/update/', normativ_answer_views.update_normativ_answer, name='update_normativ_answer'),
    path('answers/<int:pk>/delete/', normativ_answer_views.delete_normativ_answer, name='delete_normativ_answer'),
    path('check_normativs/', normativ_answer_views.check_normativs, name='check_normativs'),
    path('check_students_normativs/<int:pk>/', normativ_answer_views.check_students_normativs, name='check_students_normativs'),
]