from django.urls import path
from schedule.schedule_views import group_schedule_views, group_lesson_views

urlpatterns = [
    path('schedules/', group_schedule_views.get_group_schedule, name='group_schedule_list'),
    path('schedules/create/', group_schedule_views.create_group_schedule, name='create_group_schedule'),
    path('schedules/<int:pk>/', group_schedule_views.read_group_schedule, name='read_group_schedule'),
    path('schedules/<int:pk>/update/', group_schedule_views.update_group_schedule, name='update_group_schedule'),
    path('schedules/<int:pk>/delete/', group_schedule_views.delete_group_schedule, name='delete_group_schedule'),

    path('lessons/', group_lesson_views.get_group_lesson, name='group_lesson_list'),
    path('lessons/create/', group_lesson_views.create_group_lesson, name='create_group_lesson'),
    path('lessons/<int:pk>/', group_lesson_views.read_group_lesson, name='read_group_lesson'),
    path('lessons/<int:pk>/update/', group_lesson_views.update_group_lesson, name='update_group_lesson'),
    path('lessons/<int:pk>/delete/', group_lesson_views.delete_group_lesson, name='delete_group_lesson'),
]