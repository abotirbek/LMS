from django.urls import path
from courses.courses_views import course_views, groups_views, group_student_views, module_views, room_views, lesson_views

urlpatterns = [
    path('course_list/', course_views.get_course, name='course_list'),
    path('create_course/', course_views.create_course, name='create_course'),
    path('read_course/<int:pk>/', course_views.read_course, name='read_course'),
    path('update_course/<int:pk>/', course_views.update_course, name='update_course'),
    path('delete_course/<int:pk>/', course_views.delete_course, name='delete_course'),

    path('group_list/', groups_views.get_group, name='groups_list'),
    path('create_group/', groups_views.create_group, name='create_groups'),
    path('read_group/<int:pk>/', groups_views.read_group, name='read_groups'),
    path('update_group/<int:pk>/', groups_views.update_group, name='update_groups'),
    path('delete_group/<int:pk>/', groups_views.delete_group, name='delete_groups'),

    path('module_list', module_views.get_module, name='module_list'),
    path('create_module/', module_views.create_module, name='create_module'),
    path('read_module/<int:pk>/', module_views.read_module, name='read_module'),
    path('update_module/<int:pk>/', module_views.update_module, name='update_module'),
    path('delete_module/<int:pk>/', module_views.delete_module, name='delete_module'),

    path('room_list/', room_views.get_room, name='room_list'),
    path('create_room/', room_views.create_room, name='create_room'),
    path('read_room/<int:pk>/', room_views.read_room, name='read_room'),
    path('update_room/<int:pk>/', room_views.update_room, name='update_room'),
    path('delete_room/<int:pk>/', room_views.delete_room, name='delete_room'),

    path('lesson_list/', lesson_views.get_lesson, name='lesson_list'),
    path('create_lesson/', lesson_views.create_lesson, name='create_lesson'),
    path('read_lesson/<int:pk>/', lesson_views.read_lesson, name='read_lesson'),
    path('update_lesson/<int:pk>/', lesson_views.update_lesson, name='update_lesson'),
    path('delete_lesson/<int:pk>/', lesson_views.delete_lesson, name='delete_lesson'),

    path('group_student_list/', group_student_views.get_group_student, name='group_student_list'),
    path('create_group_student/', group_student_views.create_group_student, name='create_group_student'),
    path('read_group_student/<int:pk>/', group_student_views.read_group_student, name='read_group_student'),
    path('update_group_student/<int:pk>/', group_student_views.update_group_student, name='update_group_student'),
    path('delete_group_student/<int:pk>/', group_student_views.delete_group_student, name='delete_group_student'),
]