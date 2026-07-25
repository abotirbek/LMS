from django.urls import path
from accounts.accounts_views import register_views, student_views, teacher_views

urlpatterns = [
    path('', register_views.show_home, name='home'),
    path('register/', register_views.register, name='register'),
    path('login/', register_views.login_view, name='login'),
    path('logout/', register_views.logout_view, name='logout'),

    path('student_base/', student_views.get_student_base, name ='student_base'),
    path('student_profile/', student_views.get_student_profile, name='student_profile'),
    path('edit_student_profile/', student_views.edit_student_profile, name='edit_student_profile'),

    path('student_list/', student_views.get_student, name='student_list'),
    path('create_student/', student_views.create_student, name='create_student'),
    path('read_student/<int:pk>/', student_views.read_student, name='read_student'),
    path('update_student/<int:pk>/', student_views.update_student, name='update_student'),
    path('delete_student/<int:pk>/', student_views.delete_student, name='delete_student'),

    path('teacher_base/', teacher_views.get_teacher_base, name='teacher_base'),
    path('teacher_profile/', teacher_views.get_teacher_profile, name='teacher_profile'),
    path('edit_teacher_profile/', teacher_views.edit_teacher_profile, name='edit_teacher_profile'),

    path('teacher_list/', teacher_views.get_teacher, name='teacher_list'),
    path('create_teacher/', teacher_views.create_teacher, name='create_teacher'),
    path('read_teacher/<int:pk>/', teacher_views.read_teacher, name='read_teacher'),
    path('update_teacher/<int:pk>/', teacher_views.update_teacher, name='update_teacher'),
    path('delete_teacher/<int:pk>/', teacher_views.delete_teacher, name='delete_teacher'),
]