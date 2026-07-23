from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('schedules/', views.get_group_schedule, name='group_schedule_list'),
    path('schedules/create/', views.create_group_schedule, name='create_group_schedule'),
    path('schedules/<int:pk>/', views.read_group_schedule, name='read_group_schedule'),
    path('schedules/<int:pk>/update/', views.update_group_schedule, name='update_group_schedule'),
    path('schedules/<int:pk>/delete/', views.delete_group_schedule, name='delete_group_schedule'),

    path('lessons/', views.get_group_lesson, name='group_lesson_list'),
    path('lessons/create/', views.create_group_lesson, name='create_group_lesson'),
    path('lessons/<int:pk>/', views.read_group_lesson, name='read_group_lesson'),
    path('lessons/<int:pk>/update/', views.update_group_lesson, name='update_group_lesson'),
    path('lessons/<int:pk>/delete/', views.delete_group_lesson, name='delete_group_lesson'),
]