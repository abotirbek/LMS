from django.urls import path
from courses import views

app_name = 'courses'

urlpatterns = [
    path('course_list/', views.get_course, name='course_list'),
    path('create_course/', views.create_course, name='create_course'),
    path('read_course/<int:pk>/', views.read_course, name='read_course'),
    path('update_course/<int:pk>/', views.update_course, name='update_course'),
    path('delete_course/<int:pk>/', views.delete_course, name='delete_course'),

    path('group_list/', views.get_group, name='groups_list'),
    path('create_group/', views.create_group, name='create_groups'),
    path('read_group/<int:pk>/', views.read_group, name='read_groups'),
    path('update_group/<int:pk>/', views.update_group, name='update_groups'),
    path('delete_group/<int:pk>/', views.delete_group, name='delete_groups'),

    path('module_list', views.get_module, name='module_list'),
    path('create_module/', views.create_module, name='create_module'),
    path('read_module/<int:pk>/', views.read_module, name='read_module'),
    path('update_module/<int:pk>/', views.update_module, name='update_module'),
    path('delete_module/<int:pk>/', views.delete_module, name='delete_module'),

    path('room_list/', views.get_room, name='room_list'),
    path('create_room/', views.create_room, name='create_room'),
    path('read_room/<int:pk>/', views.read_room, name='read_room'),
    path('update_room/<int:pk>/', views.update_room, name='update_room'),
    path('delete_room/<int:pk>/', views.delete_room, name='delete_room'),

    path('lesson_list/', views.get_lesson, name='lesson_list'),
    path('create_lesson/', views.create_lesson, name='create_lesson'),
    path('read_lesson/<int:pk>/', views.read_lesson, name='read_lesson'),
    path('update_lesson/<int:pk>/', views.update_lesson, name='update_lesson'),
    path('delete_lesson/<int:pk>/', views.delete_lesson, name='delete_lesson'),

    path('group_student_list/', views.get_group_student, name='group_student_list'),
    path('create_group_student/', views.create_group_student, name='create_group_student'),
    path('read_group_student/<int:pk>/', views.read_group_student, name='read_group_student'),
    path('update_group_student/<int:pk>/', views.update_group_student, name='update_group_student'),
    path('delete_group_student/<int:pk>/', views.delete_group_student, name='delete_group_student'),
]